import '../App.css';
import '../Inventory.css';
import React from 'react';
import {Table, Button, NavbarBrand, Navbar, NavLink, Nav, Modal, ModalHeader, ModalBody, ModalFooter, Form, FormGroup, Input, Label} from 'reactstrap';

class Inventory extends React.Component{
    constructor(props){
        super(props);
        this.state={
            data:[],
            store:[],
            storeNums:[],
            storeChoice:"",
            quantityTransfer:"0",
            quantityRequest:"0",
            nameAdd:"",
            priceAdd:"0.00",
            quantityAdd:"0",
            modalID:"",
            modalStoreID:"",
            modalName:"",
            modalQuantity:"",
            addToggle:false,
            addConfirm:false,
            request:false,
            requestConfirm:false,
            transfer:false,
            transferConfirm:false,
            remove:false,
            removeConfirm:false
        }
        this.toggleRequest = this.toggleRequest.bind(this);
        this.toggleRequestConfirm = this.toggleRequestConfirm.bind(this);
        this.toggleTransfer = this.toggleTransfer.bind(this);
        this.toggleTransferConfirm = this.toggleTransferConfirm.bind(this);
        this.toggleRemove = this.toggleRemove.bind(this);
        this.toggleRemoveConfirm = this.toggleRemoveConfirm.bind(this);
        this.handleAddInput = this.handleAddInput.bind(this);
    }

    toggleRequest(){
        this.setState({request:!this.state.request})
    }

    toggleRequestConfirm(){
        this.setState({requestConfirm:!this.state.requestConfirm})
    }

    sendPostRequest(Id, Quantity){
        fetch("https://vsu7powiw8.execute-api.us-east-1.amazonaws.com/beta_v1/API/postManufacturingOrder",{
            method:'POST',
            headers:{'Content-Type': 'application/json'},
            body:JSON.stringify({"productID":Id, "quantity":Quantity})
        })
        .then((response)=>response.text())
        .then((responseText)=>{
            console.log(responseText)
        })
        .catch((error)=>{
            console.log(error)
        });
    }

    toggleTransfer(){
        this.setState({transfer:!this.state.transfer})
    }

    toggleTransferConfirm(){
        this.setState({transferConfirm:!this.state.transferConfirm})
    }

    sendTransferCommand(item, destination){
        console.log(item+" "+destination+"AAAAAAAA")
        console.log(this.state.data)
        fetch("https://api.zachctucker.com/inventory/item",{
            method:'PUT',
            headers:{'Content-Type': 'application/json'},
            body:JSON.stringify({
            "id":item,
            "itemtypeID":this.state.data[item].itemtypeid,
            "quantity":this.state.data[item].quantity,
            "storeID":destination})
        })
        .then((response)=>response.text())
        .then((responseText)=>{
            console.log(responseText)
        })
        .catch((error)=>{
            console.log(error)
        });
    }

    toggleRemove(){
        this.setState({remove:!this.state.remove})
    }

    toggleRemoveConfirm(){
        this.setState({removeConfirm:!this.state.removeConfirm})
    }

    sendDeleteItem(id){
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

    handleRequestInput(e){
        const name = e.target.name;
        const value = e.target.value;
        if(name==="quantityRequest"){
            const parse = value.replace(/^0+/,'')
            console.log(parse)
            if(parse.length===0){
                this.setState({[name]:"0"})
            }
            else{
                this.setState({[name]:parse})
            }
        }
        else{
            this.setState({ [name]: value.trim() })
        }
    }

    handleAddInput(e){
        const name = e.target.name;
        const value = e.target.value;
        if(name==="priceAdd"){
            if(value.includes(".")){
                const valArray = value.split(".")
                var first = valArray[0].replace(/^0+/,'')
                var second = valArray[1];
                if(valArray[0].length===0 || valArray[0]==="0"){
                    first = "0"
                }
                if(valArray[1].length <= 2){
                    this.setState({[name]: first+"."+second})
                }
            }
            else{
                e.preventDefault()
            }
        }
        else if(name==="quantityAdd"){
            const parse = value.replace(/^0+/,'')
            if(parse.length===0){
                this.setState({[name]:"0"})
            }
            else{
                this.setState({[name]:parse})
            }
        }
        else{
            this.setState({ [name]: value.trim() })
        }
    }

    isAddFormValid = () => {
        const {nameAdd, priceAdd, quantityAdd} = this.state
        return nameAdd && priceAdd && quantityAdd
    }

    fetchData = () => {
        fetch('https://api.zachctucker.com/inventory/item/list')
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

    setModal(index){
        this.getStores(this.state.data[index].storeid)
        this.setState({
            modalID:this.state.data[index].itemtypeid,
            modalStoreID:this.state.data[index].storeid,
            modalName:this.state.data[index].name,
            modalQuantity:this.state.data[index].quantity,
        })
    }


    fetchStores = () => {
        fetch('https://api.zachctucker.com/inventory/store/list')
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
                this.setState({store:jsonOutput})
            }
         )
    }

    getStores(ignore){
        var len = this.state.store.length;
        const arr = new Array(len);
        var index = 0;
        for(let inc = 0; inc < len; inc++){
            if(this.state.store[inc][0]!==ignore){
                arr[index]=this.state.store[inc][0];
                index++;
            }
        }
        arr.splice(arr.length-1,arr.length)
        this.setState({storeNums:arr});
    }

    componentDidMount(){
        this.fetchData();
        this.fetchStores();
    }

    render(){
        if(this.state.data == null)
            return (<div>No data</div>)
        else{
            return (
                <div className="App">
                    <Navbar color="light" light expand="md">
                        <NavbarBrand href="/inventory">Inventory</NavbarBrand>
                            <Nav className="ml-auto" navbar>
                            <NavLink href="/accounting">Accounting</NavLink>
                        </Nav>
                            <Nav className="ml-auto" navbar>
                                <NavLink href="/inventory/about">About</NavLink>
                            </Nav>
                    </Navbar>

                    <br></br>
                    <Label>
                        <b><i><u>
                            Products
                        </u></i></b>
                    </Label>

                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>StoreID</th>
                                <th>Name</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.data.map((value)=>(
                                <tr>
                                    <td>{value.itemtypeid}</td>
                                    <td>{value.storeid}</td>
                                    <td>{value.name}</td>
                                    <td>${value.price}</td>
                                    <td>{value.quantity}</td>
                                    <td>
                                        <div className="container2">

                                            <Button color="primary" onClick={()=>{
                                                this.setModal(value.itemtypeid-1)
                                                this.toggleTransfer()
                                            }}>
                                                Transfer
                                            </Button>

                                            <Button color="primary" onClick={()=>{
                                                this.setModal(value.itemtypeid-1)
                                                this.toggleRequest()
                                            }}>
                                                Request
                                            </Button>

                                        </div>
                                    </td>
                                    <td>
                                        <Button color="danger" onClick={()=>{
                                                this.setModal(value.itemtypeid-1)
                                                this.toggleRemove()
                                            }}>
                                            Remove
                                        </Button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>

                    <Modal isOpen={this.state.transfer}>
                        <ModalHeader>
                            Transfer Product?
                        </ModalHeader>
                        <ModalBody>
                            ID: {this.state.modalID}<br></br>
                            Store ID: {this.state.modalStoreID}<br></br>
                            Name: {this.state.modalName}<br></br>
                            Current Quantity: {this.state.modalQuantity}
                            <br></br>
                            <br></br>
                            <Label>
                                Transfer To:
                            </Label>
                            <br></br>
                            <select id="storeSelection" onChange={(event)=>{
                                this.setState({storeChoice:event.target.value})
                            }}>
                                 <option disabled selected hidden> -- select an option -- </option>
                                {this.state.storeNums.map((val)=>(
                                    <option value={val}>
                                        {this.state.store[val-1][1]}
                                    </option>
                                ))}
                            </select>
                        </ModalBody>
                        <ModalFooter>
                            <div className="container2">
                                <Button color="success" disabled={this.state.storeChoice===""} onClick={() =>{
                                    this.sendTransferCommand(this.state.modalID, this.state.storeChoice)
                                    this.setState({storeChoice:""})
                                    this.toggleTransfer()
                                    this.toggleTransferConfirm()
                                }}>
                                    Confirm
                                </Button>
                                <Button color="danger" onClick={()=>{
                                    this.setState({storeChoice:""})
                                    this.toggleTransfer()
                                }}>Cancel</Button>
                            </div>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.transferConfirm}>
                        <ModalBody>
                            Transfer confirmed!
                        </ModalBody>
                        <ModalFooter>
                            <Button onClick={this.toggleTransferConfirm}>
                                Complete
                            </Button>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.request}>
                        <ModalHeader>
                            Request Product?
                        </ModalHeader>
                        <ModalBody>
                            ID: {this.state.modalID}<br></br>
                            Store ID: {this.state.modalStoreID}<br></br>
                            Name: {this.state.modalName}<br></br>
                            Current Quantity: {this.state.modalQuantity}
                            <br></br>
                            <br></br>
                            <Form>
                                <Label for="productQuantityRequest">Request Quantity:</Label>
                                <Input
                                    type="number"
                                    name="quantityRequest"
                                    id="productQuantityRequest"
                                    min={1}
                                    placeholder="0"
                                    onChange={(event)=>{
                                        if(event.target.value<=0){
                                            event.target.value=1
                                        }
                                        else{
                                            this.setState({quantityRequest:event.target.value})
                                        }
                                    }}
                                    onKeyPress={(event)=>{
                                        event.preventDefault()
                                    }}
                                    >
                                </Input>
                            </Form>
                        </ModalBody>
                        <ModalFooter>
                            <div className="container2">
                                <Button color="success" disabled={this.state.quantityRequest===0} onClick={() =>{
                                    this.toggleRequest()
                                    this.toggleRequestConfirm()
                                    this.sendPostRequest(this.state.modalID, this.state.quantityRequest)
                                    this.setState({quantityRequest:0})
                                }}>
                                    Confirm
                                </Button>
                                <Button color="danger" onClick={()=>{
                                this.toggleRequest()
                                this.setState({quantityRequest:0})
                                }}>
                                    Cancel
                                </Button>
                            </div>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.requestConfirm}>
                        <ModalBody>
                            Request confirmed!
                        </ModalBody>
                        <ModalFooter>
                            <Button onClick={this.toggleRequestConfirm}>
                                Complete
                            </Button>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.remove}>
                        <ModalHeader>
                            Remove Product?
                        </ModalHeader>
                        <ModalBody>
                            ID: {this.state.modalID}<br></br>
                            Store ID: {this.state.modalStoreID}<br></br>
                            Name: {this.state.modalName}<br></br>
                            Current Quantity: {this.state.modalQuantity}
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
                            Add product
                        </Button>
                    </div>

                    <Modal isOpen={this.state.addToggle}>
                        <ModalHeader>
                            Add Product?
                        </ModalHeader>
                        <ModalBody>
                            <Form>
                                <FormGroup>
                                    <Label for="productNameAdd">Product Name</Label>
                                    <Input
                                    value={this.state.nameAdd}
                                    type="email" name="nameAdd"
                                    id="productNameAdd"
                                    onChange={(event)=>this.handleAddInput(event)}>
                                    </Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label for="productPriceAdd">Price</Label>
                                    <br></br>
                                    <div className="container2">
                                        $
                                        <Input
                                        value={this.state.priceAdd}
                                        type="email" name="priceAdd"
                                        id="productPriceAdd"
                                        onChange={(event)=>this.handleAddInput(event)}
                                        onKeyPress={(event)=>{
                                            if(!/[0-9]/.test(event.key)){
                                                event.preventDefault();
                                            }
                                        }}>
                                        </Input>
                                    </div>
                                </FormGroup>
                                <FormGroup>
                                    <Label for="productQuantityAdd">Quantity</Label>
                                    <Input
                                    type="number"
                                    name="quantityAdd"
                                    id="productQuantityAdd"
                                    min={1}
                                    placeholder="1"
                                    onChange={(event)=>{
                                        if(event.target.value<=0){
                                            event.target.value=1
                                        }
                                        else{
                                            this.setState({quantityRequest:event.target.value})
                                        }
                                    }}
                                    >
                                </Input>
                                </FormGroup>
                            </Form>
                        </ModalBody>
                        <ModalFooter>
                            <div className="container2">
                                <Button color="success" disabled={!this.isAddFormValid()} onClick={() =>{
                                    this.addToggle()
                                    this.addConfirmToggle()
                                    this.setState({nameAdd:"", priceAdd:"0.00", quantityAdd:"0"})
                                }}>
                                    ADD
                                </Button>
                                <Button color="danger" onClick={()=>{
                                    this.addToggle()
                                    this.setState({nameAdd:"", priceAdd:"0.00", quantityAdd:"0"})
                                }}>
                                    Cancel
                                </Button>
                            </div>
                        </ModalFooter>
                    </Modal>

                    <Modal isOpen={this.state.addConfirm}>
                        <ModalBody>
                            Added Product confirmed!
                        </ModalBody>
                        <ModalFooter>
                            <Button onClick={this.addConfirmToggle}>
                                Complete
                            </Button>
                        </ModalFooter>
                    </Modal>

                    <br></br>
                    <br></br>
                    <br></br>

                    <Label>
                        <b><i><u>
                            Stores
                        </u></i></b>
                    </Label>

                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th>StoreID</th>
                                <th>Name</th>
                                <th>Capacity</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.store.map((value)=>(
                                <tr>
                                    <td>{value[0]}</td>
                                    <td>{value[1]}</td>
                                    <td>{value[2]}</td>
                                    <td>
                                        <Button color="danger" onClick={()=>{
                                                this.setModal(value.itemtypeid-1)
                                                this.toggleRemove()
                                            }}>
                                            Remove
                                        </Button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>

                    <div className="container2">
                        <Button color="success" disabled={this.state.store.length===0}>
                            Add store
                        </Button>
                    </div>
                </div>
            );
        }
    }
}
  export default Inventory;