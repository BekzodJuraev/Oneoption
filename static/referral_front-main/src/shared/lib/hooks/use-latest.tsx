import { useLayoutEffect, useRef } from "react";

export const useLatest = <V,>(value: V) => {
    const valueRef = useRef(value);

    useLayoutEffect(() => {
        valueRef.current = value;
    });

    return valueRef.current;
};
