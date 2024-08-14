import styled, { css } from "styled-components";
import { ThemeType } from "@/app/styles/themes/default-theme";

type Color = ThemeType["color"];

type StringObject = Record<string, unknown>;

type FlattenObjectKeys<T extends StringObject, K = keyof T> = K extends string
    ? T[K] extends StringObject
        ? `${K}.${FlattenObjectKeys<T[K]>}`
        : `${K}`
    : never;

type ColorKeys = FlattenObjectKeys<Color>;

interface StyledButtonProps {
    color?: ColorKeys;
    background?: ColorKeys;
}

type Width = "w-full" | "w-min" | "w-max" | "w-fit";
type WidthRecord = Record<Width, boolean>;

type OneTyp<T> = {
    [K in keyof T]: { [P in K]: boolean } & Partial<{
        [Q in Exclude<keyof T, K>]: never;
    }>;
}[keyof T];

type W =
    | (OneTyp<WidthRecord> & {
          width?: never;
      })
    | ({
          [T in Width]?: never;
      } & { width: `${number}${"px" | "rem"}` });

const width = (props: W) => {
    if (props.width !== undefined) {
        return css`
            width: ${props.width};
        `;
    }

    switch (true) {
        case "w-full" in props:
            return css`
                width: 100%;
            `;
        case "w-min" in props:
            return css`
                width: min-content;
            `;
        case "w-max" in props:
            return css`
                width: max-content;
            `;
        case "w-fit" in props:
            return css`
                width: fit-content;
            `;
        default:
            break;
    }
};

// const flattenTransformation = (obj)

export const StyledButton = styled.button<StyledButtonProps & W>`
    position: relative;
    isolation: isolate;
    /* padding-block: 0.5rem;
    padding-inline: 5rem; */

    clip-path: border-box xywh(-4px 0 calc(100% + 17px) 100% round 0.5rem);

    &::after {
        content: "";
        position: absolute;
        inset: 0 0 0 -20px;
        background: yellowgreen;
        z-index: -1;
        transform: skew(35deg);
        border-radius: 0.5rem;
        border: 2px solid white;
    }

    &::before {
        content: "";
        position: absolute;
        inset: 0 0 0 -4px;
        border-left: 2px solid white;
        border-top: 2px solid white;
        border-bottom: 2px solid white;
        clip-path: polygon(-5px 0, 50% 0, 50% 100%, -5px 100%);

        border-radius: 0.5rem;
    }
`;

// type MyType = {
//     key1: string;
//     key2: number;
//     key3: boolean;
// };

// type OneOfMyType<K extends string, V = any> = {
//     [P in K]: { [Q in P]: V } & Partial<{ [Q in Exclude<K, P>]: never }>;
// }[K];

// // type OneOfMyType<K extends string, V = any> = {
// //     [P in K]: Record<P, V> &
// //         Partial<Record<Exclude<K, P>, never>> extends infer O
// //         ? { [Q in keyof O]: O[Q] }
// //         : never;
// // }[K];

// type OneOfType<K extends string, V extends object> = {
//     [P in K]: { [Q in P]: V[Q] } & Partial<{ [Q in Exclude<K, P>]: never }>;
// }[K];

// // type OneType<T, K = keyof T> = {
// //     [P in keyof T]: { [Q in P]: K } & Partial<{
// //         [Q in Exclude<K, P>]: never;
// //     }>;
// // }[K];

// type OneType<T, K extends keyof T> = {
//     [P in keyof T]: { [Q in P]: T[K] } & Partial<{
//         [Q in Exclude<keyof T, P>]: never;
//     }>;
// }[K];

// type C = OneType<MyType, "key1">;

// type MyObject = OneOfType<"key1" | "key2" | "key3", MyType>;

// // Пример использования
// const myValue1: OneOfMyType<MyType> = { key1: "value1" }; // Верно
// const myValue2: OneOfMyType<MyType> = { key2: 42 }; // Верно
// const myValue3: OneType<MyType> = { key3: true }; // Верно
// const myValue4: OneType<MyType> = { key1: "value", key2: 42 };

// console.log(myValue1, myValue2, myValue3, myValue4);
