import { Outlet } from "react-router-dom";

import { Header } from "@/widgets/header/header";

export const AppLayout = () => {
    return (
        <>
            <Header />
            <main className="container">
                <Outlet />
            </main>
        </>
    );
};
