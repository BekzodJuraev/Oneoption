import { useId } from "react";
import { Link, useNavigate } from "react-router-dom";

import { cn } from "@/shared/lib";

import { useSignInMutation } from "@/shared/api";

import { EmailIcon, PasswordIcon } from "@/entities/user/assets";
import { Checkbox } from "@/shared/ui/checkbox";

interface AuthenticationFormProps extends React.ComponentProps<"form"> {}

interface FormFields {
    email: HTMLInputElement;
    password: HTMLInputElement;
}

export const AuthenticationForm: React.FC<AuthenticationFormProps> = ({
    className,
    ...props
}) => {
    const emailId = useId();
    const passwordId = useId();

    const navigate = useNavigate();
    const [authenticate] = useSignInMutation();

    const onSubmitHandler: React.FormEventHandler<
        HTMLFormElement & FormFields
    > = async event => {
        event.preventDefault();
        const { email, password } = event.currentTarget;

        try {
            await authenticate({
                email: email.value,
                password: password.value
            }).unwrap();

            navigate("/");
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form
            onSubmit={onSubmitHandler}
            className={cn("gap-y-6-8-xs-md", className)}
            {...props}
        >
            <fieldset className="grid gap-y-2-4-xs-md">
                <div className="flex gap-x-2-4-xs-md">
                    <label
                        htmlFor={emailId}
                        className="aspect-square h-full place-content-center rounded-lg bg-white"
                    >
                        <EmailIcon className="text-2xl-4xl-xs-md text-violet-primary" />
                        <span className="sr-only">Email</span>
                    </label>
                    <input
                        id={emailId}
                        type="email"
                        name="email"
                        required
                        autoComplete="off"
                        placeholder="Почта"
                        className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                    />
                </div>

                <div className="flex gap-x-2-4-xs-md">
                    <label
                        htmlFor={passwordId}
                        className="aspect-square h-full place-content-center rounded-lg bg-white"
                    >
                        <PasswordIcon className="text-2xl-4xl-xs-md text-violet-primary" />
                        <span className="sr-only">Пароль</span>
                    </label>
                    <input
                        id={passwordId}
                        type="password"
                        name="password"
                        required
                        placeholder="Пароль"
                        className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                    />
                </div>
            </fieldset>

            <fieldset className="flex items-center justify-between text-lg text-sm-lg-xs-md ">
                <label className="grid grid-cols-[auto_auto] place-items-center gap-x-2">
                    <Checkbox className="checkbox size-6-8-xs-md" />
                    <span className="leading-none">Запомнить меня</span>
                </label>

                <Link
                    to="/password/recover"
                    className="underline underline-offset-2"
                >
                    Забыли пароль?
                </Link>
            </fieldset>
        </form>
    );
};
