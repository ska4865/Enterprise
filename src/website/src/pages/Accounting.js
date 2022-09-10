import '../App.css';
import '../Accounting.css';
import React from 'react';
import {Table, Button, NavbarBrand, Navbar, NavLink, Nav, Modal, ModalHeader, ModalBody, ModalFooter, Form, FormGroup, Input, Label} from 'reactstrap';

class Accounting extends React.Component{

    constructor(props){
        super(props);
        this.state={
            data:[],
            transaction:[],
            nameAdd:"",
            budgetAdd:"",
            modalID:"",
            modalName:"",
            modalBudget:"",
            addToggle:false,
            addConfirm:false,
            remove:false,
            removeConfirm:false
        }
        this.toggleRemove = this.toggleRemove.bind(this);
        this.toggleRemoveConfirm = this.toggleRemoveConfirm.bind(this);
        this.handleAddInput = this.handleAddInput.bind(this);
    }

    toggleRemove(){
        this.setState({remove:!this.state.remove})
    }

    toggleRemoveConfirm(){
        this.setState({removeConfirm:!this.state.removeConfirm})
    }

    sendDeleteAccount(id){
        fetch("https://vsu7powiw8.execute-api.us-east-1.amazonaws.com/beta_v1/API/postManufacturingOrder",{
            method:'DELETE',
            headers:{'Content-Type': 'application/json'},
            body:JSON.stringify({"id":id})
        })
        .then((response)=>response.text())
        .then((responseText)=>{
            console.log(responseText)
        })
        .catch((error)=>{
            console.log(error)
        });

    }

    addToggle = () => {
        this.setState({addToggle:!this.state.addToggle})
    }

    addConfirmToggle = () => {
        this.setState({addConfirm:!this.state.addConfirm})
    }

    isAddFormValid = () => {
        const {nameAdd, budgetAdd} = this.state
        return nameAdd && budgetAdd
    }

    handleAddInput(e){
        const name = e.target.name;
        const value = e.target.value;
        this.setState({ [name]: value.trim() })
    }

    setModal(index){
        this.setState({
            modalID:this.state.data[index].id,
            modalName:this.state.data[index].name,
            modalBudget:this.state.data[index].budget
        })
    }

    fetchData = () => {
        fetch('https://api.zachctucker.com/accounting/account/list')
         .then(
             (response) =>{
                if(response.ok){
                    return response.json()
                }
                else{
                    return []
                }
             }
         )
         .then (jsonOutput =>
            {
                this.setState({data:jsonOutput})
            }
         )
    }

    fetchTransactions = () => {
        fetch('https://api.zachctucker.com/accounting/transaction/list')
         .then(
             (response) =>{
                if(response.ok){
                    return response.json()
                }
                else{
                    return []
                }
             }
         )
         .then (jsonOutput =>
            {
                this.setState({data:jsonOutput})
            }
         )
    }

    componentDidMount(){
        this.fetchData()
    }

    render(){
        if(this.state.data == null)
            return (<div>No data</div>)
        else{
            return(
            <div className="App">
                <Navbar color="light" light expand="md">
                    <NavbarBrand href="/accounting">Accounting</NavbarBrand>
                        <Nav className="ml-auto" navbar>
                            <NavLink href="/inventory">Inventory</NavLink>
                        </Nav>
                        <Nav className="ml-auto" navbar>
                            <NavLink href="/accounting/about">About</NavLink>
                        </Nav>
                </Navbar>

                <br></br>
                <Label>
                    <b><i><u>
                        Accounts
                    </u></i></b>
                </Label>

                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Budget</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.data.map((value)=>(
                            <tr>
                                <td>{value.id}</td>
                                <td>{value.name}</td>
                                <td>${value.budget}</td>
                                <td>
                                    <Button color="danger" onClick={()=>{
                                            this.setModal(value.id-1)
                                            this.toggleRemove()
                                        }}>
                                        Remove
                                    </Button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </Table>

                <Modal isOpen={this.state.remove}>
                        <ModalHeader>
                            Remove Account?
                        </ModalHeader>
                        <ModalBody>
                            ID: {this.state.modalID}<br></br>
                            Name: {this.state.modalName}<br></br>
                            Current Budget: ${this.state.modalBudget}
                        </ModalBody>
                        <ModalFooter>
                            <div className="container2">
                                <Button color="success" onClick={() =>{
                                    this.toggleRemove()
                                    this.toggleRemoveConfirm()
                                }}>
                                    REMOVE
                                </Button>
                                <Button color="danger" onClick={this.toggleRemove}>Cancel</Button>
                            </div>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.removeConfirm}>
                        <ModalBody>
                            Removal confirmed!
                        </ModalBody>
                        <ModalFooter>
                            <Button onClick={this.toggleRemoveConfirm}>
                                Complete
                            </Button>
                        </ModalFooter>
                    </Modal>

                <div className="container2">
                    <Button color="success" disabled={this.state.data.length===0} onClick={this.addToggle}>
                        Add account
                    </Button>
                </div>

                <Modal isOpen={this.state.addToggle}>
                    <ModalHeader>
                        Add Account?
                    </ModalHeader>
                    <ModalBody>
                        <Form>
                            <FormGroup>
                                    <Label for="accountNameAdd">Account Name</Label>
                                    <Input
                                    value={this.state.nameAdd}
                                    type="email" name="nameAdd"
                                    id="accountNameAdd"
                                    onChange={(event)=>this.handleAddInput(event)}>
                                    </Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label for="accountBudgetAdd">Price</Label>
                                    <br></br>
                                    <div className="container2">
                                        $
                                        <Input
                                        value={this.state.budgetAdd}
                                        type="email" name="budgetAdd"
                                        id="accountBudgetAdd"
                                        onChange={(event)=>this.handleAddInput(event)}
                                        onKeyPress={(event)=>{
                                            if(!/[0-9]/.test(event.key)){
                                                event.preventDefault();
                                            }
                                        }}>
                                        </Input>
                                    </div>
                                </FormGroup>
                            </Form>
                        </ModalBody>
                        <ModalFooter>
                            <div className="container2">
                                <Button color="success" disabled={!this.isAddFormValid()} onClick={() =>{
                                    this.addToggle()
                                    this.addConfirmToggle()
                                    this.setState({nameAdd:"", budgetAdd:""})
                                }}>
                                    ADD
                                </Button>
                                <Button color="danger" onClick={()=>{
                                    this.addToggle()
                                    this.setState({nameAdd:"", budgetAdd:""})
                                }}>
                                    Cancel
                                </Button>
                            </div>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.addConfirm}>
                        <ModalBody>
                            Added Account confirmed!
                        </ModalBody>
                        <ModalFooter>
                            <Button onClick={this.addConfirmToggle}>
                                Complete
                            </Button>
                        </ModalFooter>
                    </Modal>

                    <br></br>
                    <br></br>
                   <Label>
                        <b><i><u>
                            Transactions
                        </u></i></b>
                    </Label>

                    <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>AccountID</th>
                            <th>Amount</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.transaction.map((value)=>(
                            <tr>
                                <td>{value.accountid}</td>
                                <td>{value.amount}</td>
                                <td>
                                    <Button color="danger" onClick={()=>{
                                            console.log("TESTING")
                                        }}>
                                        ???
                                    </Button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        )}
    }
}
export default Accounting;