import '../App.css';
import '../Inventory.css';
import React from 'react';
import {NavbarBrand, Navbar, NavLink, Nav} from 'reactstrap';

class AboutAcc extends React.Component{

    render(){
        return(
            <div>
                <Navbar color="light" light expand="md">
                    <NavbarBrand href="/accounting">Accounting</NavbarBrand>
                        <Nav className="ml-auto" navbar>
                            <NavLink href="/inventory">Inventory</NavLink>
                        </Nav>
                        <Nav className="ml-auto" navbar>
                            <NavLink href="/accounting/about">About</NavLink>
                        </Nav>
                </Navbar>

                <p>Developers:<br></br>
                John Davidson<br></br>
                Zach Tucker<br></br>
                Sakai Alexander
                </p>
            </div>
        )
    }
}
export default AboutAcc;