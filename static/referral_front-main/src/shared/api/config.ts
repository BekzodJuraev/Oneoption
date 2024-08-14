import {
    BaseQueryFn,
    FetchArgs,
    fetchBaseQuery,
    FetchBaseQueryError
} from "@reduxjs/toolkit/query/react";

import { RootStore } from "@/app/providers/redux/types";

const baseQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_BASE_API_URL,
    prepareHeaders: (headers, { getState }) => {
        const token = (getState() as RootStore).auth.token;

        if (token) {
            headers.set("Authorization", `Token ${token}`);
        }

        return headers;
    }
});

export const baseQueryWithLogout: BaseQueryFn<
    string | FetchArgs,
    unknown,
    FetchBaseQueryError
> = async (args, api, extraOptions) => {
    const result = await baseQuery(args, api, extraOptions);

    if (result.error && result.error.status === 401) {
        api.dispatch({ type: "auth/logout" });
    }

    return result;
};
