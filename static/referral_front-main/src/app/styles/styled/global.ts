import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
    *,
    *::after,
    *::before {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html {
        min-height: 100dvh;
        height: 100%;
        scrollbar-gutter: stable;
    }

    body {
        min-width: 340px;
        min-height: 100dvh;
        height: 100%;
    }

    img,
    svg {
        max-width: 100%;
        height: auto;
        vertical-align: middle;
        font-style: italic;
        background-repeat: no-repeat;
        background-size: cover;
        shape-margin: 0.75rem;
    }

    #root {
        width: calc(100dvw - 4rem);
        min-width: 1280px;
        margin-inline: auto;
    }
`;
