import { useEffect, useMemo, useRef } from "react";
import { useAppDispatch, useStateSelector } from "@/app/providers/redux/hooks";
import { userApi } from "@/entities/user/api";
import { StartQueryActionCreatorOptions } from "@reduxjs/toolkit/query";

const api = {
    user: {
        balance: userApi.useFetchUserBalanceQuery,
        data: userApi.useFetchUserDataQuery
    }
};

type StringObject = Record<string, unknown>;

type FlattenedObjectKeys<T extends StringObject, K = keyof T> = K extends string
    ? T[K] extends StringObject
        ? `${K}.${FlattenedObjectKeys<T[K]>}`
        : `${K}`
    : never;

export type Api = typeof api;

export type ApiKeys = FlattenedObjectKeys<Api>;

export type GetByFlattenKey<
    T extends StringObject,
    K extends string
> = K extends `${infer K1}.${infer K2}`
    ? T[K1] extends StringObject
        ? GetByFlattenKey<T[K1], K2>
        : never
    : K extends keyof T
      ? T[K]
      : never;

type E = GetByFlattenKey<Api, "user.balance">;

// export const getApi = <T extends ApiKeys>(
//     schema: T
// ): GetByFlattenKey<Api, T> => {
//     const keys = schema.split(".") as Array<keyof Api>;
//     let result: any = api;

//     for (const key of keys) {
//         result = result[key];
//     }

//     return result as GetByFlattenKey<Api, T>;
// };

const reducer = <T extends StringObject, K extends keyof T>(acc: T, key: K) => {
    if (typeof acc[key] === "object" && acc[key] !== null) {
        return acc[key];
    }
    return acc;
};

export const getApi = <T extends ApiKeys>(schema: T) => {
    return schema.split(".").reduce(reducer, api);
};

export type FunctionArgs<T extends StringObject, K extends string> =
    GetByFlattenKey<T, K> extends { initiate: (...args: any) => any }
        ? Parameters<GetByFlattenKey<T, K>["initiate"]>[0]
        : never;

export type Response<T extends StringObject, K extends string> =
    GetByFlattenKey<T, K> extends { initiate: (...args: any) => any }
        ? ReturnType<GetByFlattenKey<T, K>["initiate"]>
        : never;

export const useApi = <T extends ApiKeys>(
    schema: T,
    args: FunctionArgs<Api, T>,
    options?: StartQueryActionCreatorOptions
) => {
    const dispatch = useAppDispatch();

    useEffect(() => {
        const result = dispatch(getApi(schema).initiate(args, options));

        return result.unsubscribe;
    }, [dispatch, schema, args, options]);
};

import type {
    BaseQueryFn,
    QueryArgFrom,
    QueryDefinition
} from "@reduxjs/toolkit/query";
import type { TypedUseQuery } from "@reduxjs/toolkit/query/react";

export const useYouQueryWrapper = <
    ResultType,
    QueryArg,
    BaseQuery extends BaseQueryFn,
    D extends QueryDefinition<QueryArg, BaseQuery, any, ResultType>
    // T extends ApiKeys
>(
    useQueryHook: TypedUseQuery<ResultType, QueryArg, BaseQuery>,
    // schema: T,
    args: QueryArgFrom<D>
) => {
    // const hook = getApi(schema) as TypedUseQuery<
    //     ResultType,
    //     QueryArg,
    //     BaseQuery
    // >;

    const { data, isLoading } = useQueryHook(args);

    return data;
};
