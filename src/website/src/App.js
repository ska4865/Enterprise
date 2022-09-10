import './App.css';
import Inventory from "./pages/Inventory";
import AboutInv from "./pages/AboutInv";
import Accounting from "./pages/Accounting";
import AboutAcc from "./pages/AboutAcc";
import {Routes, Route, Navigate} from "react-router-dom";

function App(){
    return(
        <div>
            <Routes>
                <Route path="/" element={<Navigate to="inventory"/>}/>
                <Route path="*" element={<Navigate to="/"/>}/>

                <Route path="/inventory/" element={<Inventory/>}/>
                <Route path="/inventory/about/" element={<AboutInv/>}/>
                <Route path="/accounting/" element={<Accounting/>}/>
                <Route path="/accounting/about/" element={<AboutAcc/>}/>
            </Routes>
        </div>
    )
}

export default App;
