import type {
    BaseQueryFn,
    QueryArgFrom,
    QueryDefinition
} from "@reduxjs/toolkit/query";
import type { TypedUseQuery } from "@reduxjs/toolkit/query/react";

export const useFetch = <
    ResultType,
    QueryArg,
    BaseQuery extends BaseQueryFn,
    D extends QueryDefinition<QueryArg, BaseQuery, any, ResultType>
>(
    useQuery: TypedUseQuery<ResultType, QueryArg, BaseQuery>,
    args: QueryArgFrom<D>
) => {
    return useQuery(args);
};
