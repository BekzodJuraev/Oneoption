import {
    useFetchUserDataQuery,
    FetchUserDataResponse
} from "@/entities/user/api";

interface FetchUserDataProps {
    renderSuccess: (data: FetchUserDataResponse) => React.ReactElement;
    loadingFallback?: React.ReactNode;
    renderError?: (error: string) => React.ReactElement;
}

export const FetchUserData: React.FC<FetchUserDataProps> = ({
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
}) => {
    const { data, isLoading, isError, error } = useFetchUserDataQuery();

    if (isLoading) return loadingFallback;

    if (isError) return renderError(error?.data?.details);

    if (data) return renderSuccess(data);

    return <pre>Нет данных</pre>;
};
