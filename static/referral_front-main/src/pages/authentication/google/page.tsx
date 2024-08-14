import { useEffect } from "react";
import { Navigate } from "react-router-dom";
import { useAppDispatch } from "@/app/providers/redux/hooks";
import { login } from "@/shared/api/authSlice";

export const GoogleAuthenticationPage = () => {
    // const navigate = useNavigate();
    const dispatch = useAppDispatch();

    useEffect(() => {
        const queryString = window.location.search;

        const searchParams = new URLSearchParams(queryString);

        if (searchParams.has("token")) {
            dispatch(login({ token: searchParams.get("token")! }));
        }

        // navigate("/");
    }, []);

    return <Navigate to="/" />;
};
