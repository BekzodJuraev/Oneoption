import type {
    BaseQueryFn,
    QueryArgFrom,
    QueryDefinition
} from "@reduxjs/toolkit/query";
import type {
    TypedUseQuery,
    TypedUseQueryHookResult
} from "@reduxjs/toolkit/query/react";

import { useFetch } from "@/shared/lib/hooks";

type Fetch<
    ResultType,
    QueryArg,
    BaseQuery extends BaseQueryFn,
    D extends QueryDefinition<QueryArg, BaseQuery, any, ResultType>
> = {
    useQuery: TypedUseQuery<ResultType, QueryArg, BaseQuery>;
    args: QueryArgFrom<D>;
    renderSuccess: (
        data: TypedUseQueryHookResult<
            ResultType,
            QueryArgFrom<D>,
            BaseQueryFn,
            any
        >["data"]
    ) => React.ReactElement;
    loadingFallback?: React.ReactNode;
    renderError?: (error: string) => React.ReactElement;
};

export const Fetch = <
    ResultType,
    QueryArg,
    BaseQuery extends BaseQueryFn,
    D extends QueryDefinition<QueryArg, BaseQuery, any, ResultType>
>({
    useQuery,
    args,
    renderSuccess,
    loadingFallback = (
        <div className="flex w-full items-center justify-center px-3">
            Loading...
        </div>
    ),
    renderError = error => (
        <pre className="self-center text-center text-red-700">
            {error || "Неизвестная ошибка"}
        </pre>
    )
}: Fetch<ResultType, QueryArg, BaseQuery, D>) => {
    const { data, isLoading, isSuccess, isError, error } = useFetch(
        useQuery,
        args
    );

    if (isLoading) return loadingFallback;

    if (isError) return renderError(error?.data?.message);

    if (isSuccess) return renderSuccess(data);

    return <></>;
};
