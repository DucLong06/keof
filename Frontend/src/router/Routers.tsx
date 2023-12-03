import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import Register from "../pages/Account/Register/Register";

const Routers = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Register />}></Route>
            </Routes>
        </BrowserRouter>
    );
};

export default Routers;
