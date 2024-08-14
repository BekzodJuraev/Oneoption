import { useMemo } from "react";

import { useStateSelector } from "@/app/providers/redux/hooks";

export const useAuth = () => {
    const token = useStateSelector(state => state.auth.token);
    const isAuthenticated = useStateSelector(
        state => state.auth.isAuthenticated
    );

    return useMemo(
        () => ({
            token,
            isAuthenticated
        }),
        [token, isAuthenticated]
    );
};
