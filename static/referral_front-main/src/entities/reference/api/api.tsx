import { rootApi } from "@/shared/api";

export const referenceApi = rootApi
    .enhanceEndpoints({ addTagTypes: ["Reference"] })
    .injectEndpoints({
        endpoints: builder => ({
            fetchReferenceStatistic: builder.query<
                {
                    all_click: 0;
                    register_count: 0;
                    deposit: string;
                    ftd_count: 0;
                    ftd_sum: string;
                    witdraw_ref: string;
                    oborot: string;
                },
                void
            >({
                query: () => "/profile/mainpage"
            }),
            fetchReferenceChartData: builder.query<
                {
                    clicks: number;
                    register_count: number;
                    ftd_count: number;
                    day?: string;
                },
                { frequency: "daily" | "weekly" | "monthly" }
            >({
                query: ({ frequency }) => `/profile/mainpage/chart_${frequency}`
            })
        })
    });

export const {
    useFetchReferenceStatisticQuery,
    useLazyFetchReferenceStatisticQuery,
    useFetchReferenceChartDataQuery,
    useLazyFetchReferenceChartDataQuery
} = referenceApi;
