import React from "react";
import ReactDOM from "react-dom/client";

import { RouterProvider } from "@/app/providers/router";
import { ReduxProvider } from "@/app/providers/redux";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>
        <ReduxProvider>
            <RouterProvider />
        </ReduxProvider>
    </React.StrictMode>
);
