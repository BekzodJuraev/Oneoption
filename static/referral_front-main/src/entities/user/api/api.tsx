import { rootApi, SuccessResponse } from "@/shared/api";

import type { FetchUserDataResponse, FetchUserBalanceResponse } from "./types";

export const userApi = rootApi
    .enhanceEndpoints({ addTagTypes: ["User"] })
    .injectEndpoints({
        endpoints: builder => ({
            fetchUserData: builder.query<FetchUserDataResponse, void>({
                query: () => "/profile/",
                providesTags: ["User"]
            }),
            fetchUserBalance: builder.query<FetchUserBalanceResponse, void>({
                query: () => "/profile/balance"
            }),
            updateUserPhoto: builder.mutation<SuccessResponse, File>({
                query: photo => {
                    const formData = new FormData();
                    formData.append("photo", photo);
                    return {
                        url: "/profile/",
                        method: "PATCH",
                        body: formData,
                        headers: {
                            Accept: "application/json"
                        }
                    };
                },
                invalidatesTags: (result, error) => (error ? [] : ["User"])
            })
        })
    });

export const {
    useFetchUserDataQuery,
    useLazyFetchUserDataQuery,
    useFetchUserBalanceQuery,
    useLazyFetchUserBalanceQuery,
    useUpdateUserPhotoMutation
} = userApi;
