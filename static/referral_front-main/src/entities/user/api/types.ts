export interface FetchUserDataResponse {
    first_name: string;
    last_name: string;
    email: string;
    photo?: string;
    level?: number;
    ftd_count: number;
}

export interface FetchUserBalanceResponse {
    total_income: string;
    income_oborot: string;
    income_doxod: string;
}

export interface AuthenticateUserRequest {
    email: string;
    password: string;
}

export interface UpdateUserPhotoRequest {
    photo: string;
}
