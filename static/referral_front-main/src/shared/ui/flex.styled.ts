import styled from "styled-components";

export const Flex = styled.div`
    display: flex;
    justify-content: ${({ className }) => {
        switch (true) {
            case className?.includes("justify-start"):
                return "flex-start";
            case className?.includes("justify-end"):
                return "flex-end";
            case className?.includes("justify-center"):
                return "center";
            case className?.includes("justify-between"):
                return "space-between";
            case className?.includes("justify-around"):
                return "space-around";
            case className?.includes("justify-evenly"):
                return "space-evenly";
            case className?.includes("justify-stretch"):
                return "stretch";

            default:
                return "center";
        }
    }};
    align-items: ${({ className }) => {
        switch (true) {
            case className?.includes("items-start"):
                return "flex-start";
            case className?.includes("items-end"):
                return "flex-end";
            case className?.includes("items-center"):
                return "center";
            case className?.includes("items-baseline"):
                return "baseline";
            case className?.includes("items-stretch"):
                return "stretch";

            default:
                return "center";
        }
    }};
`;
