import { useEffect, RefObject } from "react";

export const useOutsideClick = <T extends HTMLElement>(
    ref: RefObject<T>,
    callback: () => void,
    options?: AddEventListenerOptions
): void => {
    const handleClick = (event: MouseEvent) => {
        if (ref.current && !ref.current.contains(event.target as Node)) {
            callback();
        }
    };

    useEffect(() => {
        document.addEventListener("click", handleClick, options);

        return () => {
            document.removeEventListener("click", handleClick, options);
        };
    }, [ref, callback]);
};
