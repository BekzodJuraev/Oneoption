import { useId } from "react";
import * as StyledForm from "./form.styled";
import { Flex } from "@/shared/ui/flex.styled";

import Logo from "@/assets/logo.png";
import { PasswordIcon } from "./password.icon";

export const RecoveryPasswordForm = () => {
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
                    Восстановление <br /> пароля
                </h1>
            </StyledForm.Header>

            <StyledForm.Form>
                <p>
                    На ваш почтовый ящик отправлено письмо <br /> с кодом
                    подтверждения
                </p>

                <div>
                    <StyledForm.Label htmlFor={emailId}>
                        <PasswordIcon />
                    </StyledForm.Label>
                    <StyledForm.Input
                        id={emailId}
                        type="text"
                        placeholder="Код подтверждения"
                    />
                </div>
            </StyledForm.Form>

            <Flex
                className="justify-center"
                style={{ gap: "1rem", marginTop: "2.5rem" }}
            >
                <StyledForm.Button>Подтвердить</StyledForm.Button>
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
