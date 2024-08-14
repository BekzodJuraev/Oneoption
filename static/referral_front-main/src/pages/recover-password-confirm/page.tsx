import { useId } from "react";
import { Link, useNavigate } from "react-router-dom";

import Logo from "@/assets/logo.png";
import {
    useConfirmPasswordMutation,
    type ConfirmPasswordRequest
} from "@/shared/api";
import { PasswordIcon } from "@/entities/user/assets";

type FormField = {
    [K in keyof ConfirmPasswordRequest]: HTMLInputElement;
};

export const RecoverPasswordConfirmPage = () => {
    const formId = `form-${useId()}`;
    const newPasswordId = `password-${useId()}`;
    const confirmPasswordId = `password-${useId()}`;

    const navigate = useNavigate();
    const [confirmPassword] = useConfirmPasswordMutation();

    const onSubmitHandler: React.FormEventHandler<
        HTMLFormElement & FormField
    > = async event => {
        event.preventDefault();

        const { new_password, confirm_password } = event.currentTarget;

        try {
            await confirmPassword({
                new_password: new_password.value,
                confirm_password: confirm_password.value
            }).unwrap();
            navigate("/sign/in");
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <main className="min-h-dvh bg-[url('@/assets/bg.webp')]">
            <section className="mx-auto max-w-3xl space-y-6-8-xs-md px-4 py-8">
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
                    className="grid gap-x-2-4-xs-md"
                >
                    <div className="flex gap-x-2-4-xs-md">
                        <label
                            htmlFor={newPasswordId}
                            className="aspect-square h-full place-content-center rounded-lg bg-white"
                        >
                            <PasswordIcon className="text-2xl-4xl-xs-md text-violet-primary" />
                            <span className="sr-only">Пароль</span>
                        </label>
                        <input
                            id={newPasswordId}
                            type="password"
                            name="password"
                            autoComplete="off"
                            minLength={8}
                            maxLength={128}
                            placeholder="Пароль"
                            className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                        />
                    </div>

                    <div className="flex gap-x-2-4-xs-md">
                        <label
                            htmlFor={confirmPasswordId}
                            className="aspect-square h-full place-content-center rounded-lg bg-white"
                        >
                            <PasswordIcon className="text-2xl-4xl-xs-md text-violet-primary" />
                            <span className="sr-only">Повторите пароль</span>
                        </label>
                        <input
                            id={confirmPasswordId}
                            type="password"
                            name="password2"
                            autoComplete="off"
                            minLength={8}
                            maxLength={128}
                            placeholder="Подтвердите пароль"
                            className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                        />
                    </div>
                </form>

                <button
                    form={formId}
                    className="mx-auto block rounded-lg border-2 border-white-primary bg-white-primary py-3 text-black transition-colors duration-300 sm:px-16 mh:hover:bg-transparent mh:hover:text-white-primary"
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
