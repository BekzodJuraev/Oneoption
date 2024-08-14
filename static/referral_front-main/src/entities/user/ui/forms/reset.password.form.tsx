import { useId } from "react";
import * as StyledForm from "./form.styled";
import { Flex } from "@/shared/ui/flex.styled";

import Logo from "@/assets/logo.png";
import { EmailIcon } from "./email.icon";

export const ResetPasswordForm = () => {
    const emailId = useId();

    return (
        <StyledForm.Section>
            <StyledForm.Header>
                <img
                    src={Logo}
                    alt="Logo"
                    height="125"
                    width="220"
                />
                <h1>
                    Восстановление <br />
                    пароля
                </h1>
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
            </StyledForm.Form>

            <Flex
                className="justify-center"
                style={{ gap: "1rem", marginTop: "2.5rem" }}
            >
                <StyledForm.Button>Восстановить</StyledForm.Button>
            </Flex>

            <StyledForm.Footer>
                <p>
                    Уже зарегистрированы? <a>Войти</a>
                </p>
                <p>
                    Еще нет аккаунта? <a>Зарегистрироваться</a>
                </p>
            </StyledForm.Footer>
        </StyledForm.Section>
    );
};
