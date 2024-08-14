import styled, { css } from "styled-components";

const Section = styled.section`
    color: #fef7ff;
    font-size: 1.25rem;

    & a {
        text-decoration: underline;
        will-change: color;
        transition: color 0.3s ease-in-out;

        &:hover {
            color: #535bf2;
        }
    }
`;

const Header = styled.header`
    user-select: none;

    & > h1 {
        font-size: 84px;
        line-height: 100%;
    }

    & > p {
        margin-top: 10px;
        font-size: 2.25rem;
        line-height: 100%;
    }
`;

const Form = styled.form`
    display: grid;
    grid-row-gap: 1.5rem;
    margin-top: 50px;

    & > div {
        display: flex;
        gap: 10px;
    }
`;

const Input = styled.input.attrs({
    autoComplete: "off"
})`
    ${({ type }) => {
        switch (type) {
            case "text":
            case "email":
            case "password":
                return css`
                    flex: 1 1 auto;
                    height: 70px;
                    padding-inline: 1.5rem;
                    border-radius: 10px;
                    background-color: #fef7ff;
                    border: none;

                    font-size: 1.375rem;
                    font-family: inherit;

                    &:focus-visible {
                        outline: 2px solid #fef7ff;
                        outline-offset: 2px;
                    }

                    &::placeholder {
                        line-height: 125%;

                        color: #969696;
                    }
                `;

            case "checkbox":
                return css`
                    appearance: none;
                    -webkit-appearance: none;
                    -moz-appearance: none;

                    width: 2.5rem;
                    height: 2.5rem;

                    border: 4px solid white;
                    border-radius: 4px;

                    cursor: pointer;

                    &:checked {
                        background: url("data:image/svg+xml, %3Csvg width='40' height='40' viewBox='0 0 40 40' fill='none' xmlns='http://www.w3.org/2000/svg' %3E%3Cpath d='M32.9783 13.5L29.9233 10.4233L15.645 24.7017L10.055 19.1333L6.97833 22.1883L15.645 30.8333L32.9783 13.5Z' fill='%23FEF7FF' /%3E%3C/svg%3E")
                            no-repeat center;
                    }
                `;

            default:
                break;
        }
    }}
`;

const Label = styled.label`
    display: flex;
    justify-content: center;
    align-items: center;

    width: 70px;
    height: 70px;

    background-color: #fef7ff;
    color: #4619a6;
    border-radius: 10px;

    &:has(input[type="checkbox"]) {
        width: unset;
        height: unset;

        text-align: start;

        background-color: unset;
        color: unset;
        border-radius: unset;

        gap: 0.75rem;
    }

    cursor: pointer;
`;

const Button = styled.button`
    padding: 1rem 4rem;
    font-weight: 500;
    background-color: #ffffff;
    border-radius: 10px;
    border: 2px solid transparent;
    will-change: color, border, background-color;
    transition:
        color,
        border,
        background-color 0.3s ease-in-out;

    &:focus-visible {
        outline: 2px solid #fef7ff;
        outline-offset: 2px;
    }

    &:hover {
        color: #ffffff;
        border: 2px solid #ffffff;
        background-color: transparent;
    }

    ${({ className }) =>
        className?.includes("outlined")
            ? css`
                  background: transparent;
                  color: #fef7ff;
                  border: 1px solid #ffffff;

                  &:hover {
                      color: #000000;
                      border: 1px solid transparent;
                      background-color: #ffffff;
                  }
              `
            : null}
`;

const Footer = styled.footer`
    margin-top: 1.25rem;
`;

export { Section, Header, Form, Label, Input, Button, Footer };
