import { Outlet } from "react-router-dom";
import "./App.css";

export const App = () => {
    return (
        <main>
            <Outlet />
        </main>
    );
};
