import { useId } from "react";
import { useNavigate } from "react-router-dom";

import { useRecoverPasswordMutation } from "@/shared/api";

import Logo from "@/assets/logo.png";
import { EmailIcon } from "@/entities/user/assets";
import { Link } from "react-router-dom";

interface FormField {
    email: HTMLInputElement;
}

export const RecoverPasswordPage = () => {
    const email = `email-${useId()}`;
    const formId = `form-${useId()}`;

    const navigate = useNavigate();
    const [recoverPassword] = useRecoverPasswordMutation();

    const onSubmitHandler: React.FormEventHandler<
        HTMLFormElement & FormField
    > = async event => {
        event.preventDefault();

        const { email } = event.currentTarget;

        try {
            await recoverPassword({ email: email.value }).unwrap();
            navigate("/password/recover/confirm");
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <main className="min-h-dvh bg-[url('@/assets/bg.webp')] px-4 py-8">
            <section className="mx-auto max-w-3xl space-y-6-8-xs-md">
                <header className="space-y-2-3-xs-md">
                    <img
                        src={Logo}
                        alt="Logo"
                        height="125"
                        width="220"
                        className="mx-auto block"
                    />
                    <h1 className="text-balance text-center text-4xl-7xl-xs-md">
                        Восстановить пароль
                    </h1>
                </header>

                <form
                    id={formId}
                    onSubmit={onSubmitHandler}
                    className="grid grid-cols-[minmax(min-content,_auto)_1fr] gap-x-2-4-xs-md"
                >
                    <label
                        htmlFor={email}
                        className="aspect-square h-full place-content-center rounded-lg bg-white"
                    >
                        <EmailIcon className="text-2xl-4xl-xs-md text-violet-primary" />
                        <span className="sr-only">Email</span>
                    </label>
                    <input
                        id={email}
                        type="email"
                        name="email"
                        required
                        autoComplete="off"
                        placeholder="Почта"
                        className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                    />
                </form>

                <button
                    form={formId}
                    className="mx-auto block rounded-lg border-2 border-white-primary bg-white-primary px-16 py-3 text-black transition-colors duration-300 mh:hover:bg-transparent mh:hover:text-white-primary"
                >
                    Сбросить
                </button>

                <footer className="text-sm-lg-xs-md">
                    <p className="text-center">
                        Вы помните свой пароль?{" "}
                        <Link
                            to="/sign/in"
                            className="underline underline-offset-2"
                        >
                            Войти
                        </Link>
                    </p>
                </footer>
            </section>
        </main>
    );
};
