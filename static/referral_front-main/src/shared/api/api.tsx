import { createApi } from "@reduxjs/toolkit/query/react";
import { baseQueryWithLogout } from "@/shared/api/config";

import type {
    SignInRequest,
    SignInSuccessResponse,
    RecoverPasswordRequest,
    ConfirmPasswordRequest,
    ChangePasswordRequest,
    ChangePasswordResponse,
    SignUpRequest,
    SuccessResponse
} from "./types";

export const rootApi = createApi({
    reducerPath: "rootApi",
    baseQuery: baseQueryWithLogout,
    endpoints: builder => ({
        signIn: builder.mutation<SignInSuccessResponse, SignInRequest>({
            query: body => ({
                url: "/login/",
                method: "POST",
                body: body
            })
        }),
        signInWithGoogle: builder.query<any, void>({ query: () => "/google/" }),
        signUp: builder.mutation<SuccessResponse, SignUpRequest>({
            query: body => ({
                url: "/register/",
                method: "POST",
                body: body
            })
        }),
        recoverPassword: builder.mutation<
            SuccessResponse,
            RecoverPasswordRequest
        >({
            query: body => ({
                url: "/password_reset/",
                method: "POST",
                body: body
            })
        }),
        confirmPassword: builder.mutation<
            SuccessResponse,
            ConfirmPasswordRequest
        >({
            query: body => ({
                url: `/password_reset/${JSON.parse(localStorage.getItem("token") || "{}")?.token}`,
                method: "POST",
                body: body
            })
        }),
        changePassword: builder.mutation<
            ChangePasswordResponse,
            ChangePasswordRequest
        >({
            query: body => ({
                url: "/change_password/",
                method: "POST",
                body: body
            })
        }),
        signOut: builder.mutation<SuccessResponse, void>({
            query: () => ({
                url: "/logout/",
                method: "POST"
            })
        })
    })
});

export const {
    useSignInMutation,
    useSignInWithGoogleQuery,
    useLazySignInWithGoogleQuery,
    useSignUpMutation,
    useRecoverPasswordMutation,
    useConfirmPasswordMutation,
    useChangePasswordMutation,
    useSignOutMutation
} = rootApi;
