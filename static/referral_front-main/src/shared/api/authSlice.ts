import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { rootApi } from "./api";

type AuthorizedUser = {
    token: string;
    isAuthenticated: true;
};

type NonAuthorizedUser = {
    token: null;
    isAuthenticated: false;
};

type AuthState = AuthorizedUser | NonAuthorizedUser;

export const authSlice = createSlice({
    name: "auth",
    initialState: () => {
        const storedData = localStorage.getItem("token");

        if (!storedData)
            return {
                token: null,
                isAuthenticated: false
            };

        const { token } = JSON.parse(storedData);

        return {
            token,
            isAuthenticated: true
        } as AuthState;
    },
    reducers: {
        login: (state, action: PayloadAction<{ token: string }>) => {
            state.token = action.payload.token;
            state.isAuthenticated = true;
            localStorage.setItem(
                "token",
                JSON.stringify({ token: action.payload.token })
            );
        },
        logout: state => {
            state.token = null;
            state.isAuthenticated = false;
            localStorage.removeItem("token");
        }
    },
    extraReducers: builder => {
        builder.addMatcher(
            rootApi.endpoints.signIn.matchFulfilled,
            (state, { payload }) => {
                state.token = payload.token;
                state.isAuthenticated = true;
                localStorage.setItem(
                    "token",
                    JSON.stringify({ token: payload.token })
                );
            }
        );
    }
});

export const { reducer: authReducer, actions: authActions } = authSlice;

export const { login, logout } = authSlice.actions;
