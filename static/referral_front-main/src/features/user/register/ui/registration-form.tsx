import { useId } from "react";
import { useNavigate } from "react-router-dom";

import { cn } from "@/shared/lib";

import { useSignUpMutation } from "@/shared/api";

import { EmailIcon, PasswordIcon } from "@/entities/user/assets";
import { Checkbox } from "@/shared/ui/checkbox";

interface RegistrationFormProps extends React.ComponentProps<"form"> {}

interface FormFields {
    email: HTMLInputElement;
    password: HTMLInputElement;
    password2: HTMLInputElement;
}

export const RegistrationForm: React.FC<RegistrationFormProps> = ({
    className,
    ...props
}) => {
    const emailId = useId();
    const passwordId = useId();
    const confirmPasswordId = useId();
    const labelId = useId();

    const navigate = useNavigate();
    const [signUp] = useSignUpMutation();

    const onSubmitHandler: React.FormEventHandler<
        HTMLFormElement & FormFields
    > = async event => {
        event.preventDefault();
        const { email, password, password2 } = event.currentTarget;

        try {
            const response = await signUp({
                email: email.value,
                password: password.value,
                password2: password2.value
            }).unwrap();

            navigate("/sign/in");

            console.log(response);
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
                        autoComplete="off"
                        maxLength={255}
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
                        autoComplete="off"
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
                        maxLength={128}
                        placeholder="Подтвердите пароль"
                        className="flex-auto rounded-lg px-4-6-xs-md py-3-4-xs-md text-base-xl-xs-md text-black"
                    />
                </div>
            </fieldset>

            <fieldset className="grid grid-cols-[auto_1fr] place-items-center gap-x-2-4-xs-md text-start text-lg ">
                <Checkbox
                    aria-labelledby={labelId}
                    className="checkbox size-6-8-xs-md"
                />
                <span
                    id={labelId}
                    className="text-sm-lg-xs-md leading-none"
                >
                    Я подтверждаю, что мне исполнилось 18 лет и я принимаю
                    условия{" "}
                    <a className="text-sm-lg-xs-md underline underline-offset-2">
                        Пользовательского соглашения
                    </a>
                </span>
            </fieldset>
        </form>
    );
};
