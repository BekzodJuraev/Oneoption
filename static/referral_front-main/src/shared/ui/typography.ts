import styled from "styled-components";

interface Clamp {
    minFontSize: number;
    maxFontSize: number;
    minWidth: number;
    maxWidth: number;
    pxPerRem?: number;
}

interface TypographyProps {
    clamp?: Clamp;
}

export const Typography = styled.p<TypographyProps>`
    font-size: ${({ clamp }) => {
        if (clamp === undefined) return null;

        const minWidth = clamp.minWidth / (clamp.pxPerRem || 16);
        const maxWidth = clamp.maxWidth / (clamp.pxPerRem || 16);
        const slope =
            (clamp.maxFontSize - clamp.minFontSize) / (maxWidth - minWidth);
        const yAxisIntersection = -minWidth * slope + clamp.minFontSize;

        return `clamp(${clamp.minFontSize}rem, ${yAxisIntersection.toFixed(3)}rem + ${(slope * 100).toFixed(3)}dvw, ${clamp.maxFontSize}rem)`;
    }};
`;
