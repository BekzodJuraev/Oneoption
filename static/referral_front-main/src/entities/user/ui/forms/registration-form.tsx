import { useId } from "react";
import * as StyledForm from "./form.styled";
import { Flex } from "@/shared/ui/flex.styled";

import Logo from "@/assets/logo.png";
import { EmailIcon } from "./email.icon";
import { PasswordIcon } from "./password.icon";

export const RegistrationForm = () => {
    const emailId = useId();
    const passwordId = useId();
    const confirmPasswordId = useId();

    return (
        <StyledForm.Section>
            <StyledForm.Header>
                <img
                    src={Logo}
                    alt="Logo"
                    height="125"
                    width="220"
                />
                <h1>Регистрация</h1>
                <p>в партнерской программе</p>
            </StyledForm.Header>

            <StyledForm.Form>
                <div>
                    <StyledForm.Label htmlFor={emailId}>
                        <EmailIcon />
                    </StyledForm.Label>
                    <StyledForm.Input
                        id={emailId}
                        type="email"
                        placeholder="Почта"
                    />
                </div>

                <div>
                    <StyledForm.Label htmlFor={passwordId}>
                        <PasswordIcon />
                    </StyledForm.Label>
                    <StyledForm.Input
                        id={passwordId}
                        type="password"
                        placeholder="Пароль"
                    />
                </div>

                <div>
                    <StyledForm.Label htmlFor={confirmPasswordId}>
                        <PasswordIcon />
                    </StyledForm.Label>
                    <StyledForm.Input
                        id={confirmPasswordId}
                        type="password"
                        placeholder="Подтвердите пароль"
                    />
                </div>

                <Flex className="justify-between">
                    <StyledForm.Label>
                        <StyledForm.Input type="checkbox" />
                        <span>
                            Я подтверждаю, что мне исполнилось 18 лет и я
                            принимаю условия
                            <br /> <a>Пользовательского соглашения</a>
                        </span>
                    </StyledForm.Label>
                </Flex>
            </StyledForm.Form>

            <Flex
                className="justify-center"
                style={{ gap: "1rem", marginTop: "2.5rem" }}
            >
                <StyledForm.Button>Зарегистрироваться</StyledForm.Button>
                <StyledForm.Button className="outlined">
                    Регистрация через Google
                </StyledForm.Button>
            </Flex>

            <StyledForm.Footer>
                <p>
                    Уже зарегистрированы? <a>Войти</a>
                </p>
            </StyledForm.Footer>
        </StyledForm.Section>
    );
};
