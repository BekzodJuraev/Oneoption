import { useId } from "react";
import { Link } from "react-router-dom";

import { AuthorizationHeaderWidget } from "@/widgets/authorization-header";
import { UserAuthenticationForm } from "@/features/user/authenticate";
// import { SignInWithGoogleButton } from "@/features/user/authectication/sign-in-with-google";

export const SignInPage = () => {
    const authenticationFormId = `form-${useId()}`;

    return (
        <>
            <AuthorizationHeaderWidget>
                <hgroup>
                    <h1 className="text-4xl-7xl-xs-md">Вход</h1>
                    <p className="text-xl-4xl-xs-md">в партнерскую программу</p>
                </hgroup>
            </AuthorizationHeaderWidget>

            <UserAuthenticationForm id={authenticationFormId} />

            <div className="flex flex-col justify-center gap-2-4-xs-md text-base-xl-xs-md sm:flex-row">
                <button
                    form={authenticationFormId}
                    className="rounded-lg border-2 border-white-primary bg-white-primary py-3 text-black transition-colors duration-300 sm:px-16 mh:hover:bg-transparent mh:hover:text-white-primary"
                >
                    Войти
                </button>
                <a
                    href="/google/"
                    className="rounded-lg border-2 border-white-primary py-3 transition-colors duration-300 sm:px-16 mh:hover:bg-white-primary mh:hover:text-black"
                >
                    Войти через Google
                </a>
            </div>

            <footer className="text-sm-lg-xs-md">
                <p>
                    Еще нет аккаунта?{" "}
                    <Link
                        to="/sign/up"
                        className="underline underline-offset-2"
                    >
                        Зарегистрироваться
                    </Link>
                </p>
            </footer>
        </>
    );
};
