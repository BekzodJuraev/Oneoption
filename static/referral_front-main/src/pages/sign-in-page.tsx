import { useId } from "react";
import { UserAuthenticationForm } from "@/features/user/authenticate";

// import { useLazySignInWithGoogleQuery } from "@/shared/api";

import Logo from "@/assets/logo.png";
import { Link } from "react-router-dom";

export const SignInPage = () => {
    const authenticationFormId = `form-${useId}`;

    // const [signInWithGoogle] = useLazySignInWithGoogleQuery();

    // const authenticateWithGoogle: React.MouseEventHandler<
    //     HTMLButtonElement
    // > = async () => {
    //     try {
    //         await signInWithGoogle();
    //     } catch (error) {
    //         console.error(error);
    //     }
    // };

    return (
        <section className="min-h-dvh bg-[url('@/assets/bg.webp')]">
            <div className="mx-auto max-w-3xl space-y-6-8-xs-md px-4 py-8 text-center @container md:px-8">
                <header className="space-y-2-3-xs-md">
                    <img
                        src={Logo}
                        alt="Logo"
                        height="125"
                        width="220"
                        className="mx-auto block"
                    />
                    <h1 className="text-4xl-7xl-xs-md">Вход</h1>
                    <p className="text-xl-4xl-xs-md">в партнерскую программу</p>
                </header>

                <UserAuthenticationForm id={authenticationFormId} />

                <div className="flex flex-col justify-center gap-2-4-xs-md text-base-xl-xs-md sm:flex-row">
                    <button
                        form={authenticationFormId}
                        className="rounded-lg border-2 border-white-primary bg-white-primary py-3 text-black transition-colors duration-300 sm:px-16 mh:hover:bg-transparent mh:hover:text-white-primary"
                    >
                        {/* <button className="clip-path w-72"> */}
                        Войти
                    </button>
                    <a
                        href="/google/"
                        // onClick={authenticateWithGoogle}
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
            </div>
        </section>
    );
};
