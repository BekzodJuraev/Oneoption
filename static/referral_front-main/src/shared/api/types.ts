export interface SignInRequest {
    email: string;
    password: string;
}

export interface SignUpRequest extends SignInRequest {
    password2: string;
}

export type SuccessResponse = {
    detail: string;
};

export type SignInSuccessResponse = SuccessResponse & {
    token: string;
};

export interface RecoverPasswordRequest {
    email: string;
}

export interface ConfirmPasswordRequest {
    new_password: string;
    confirm_password: string;
}

export interface ChangePasswordRequest {
    old_password: string;
    new_password: string;
    new_password_confirm: string;
}

export interface ChangePasswordResponse extends SuccessResponse {}
