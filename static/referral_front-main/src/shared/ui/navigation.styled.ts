import styled from "styled-components";

export const StyledNavigation = styled.nav`
    & li {
        background-color: #2b2930;

        &:has(a[aria-current="page"]) {
            background-color: #793aff;
        }

        & > a {
            display: flex;
            justify-content: center;
            align-items: center;

            flex: 1 1 auto;
            height: 100%;
        }
    }
`;
