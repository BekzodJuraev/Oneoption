import { configureStore } from "@reduxjs/toolkit";

import { rootApi } from "@/shared/api";

import { authReducer } from "@/shared/api/authSlice";

export const store = configureStore({
    reducer: {
        auth: authReducer,
        [rootApi.reducerPath]: rootApi.reducer
    },
    middleware: getDefaultMiddleware =>
        getDefaultMiddleware().concat(rootApi.middleware)
});
