import { useCallback, useLayoutEffect, useRef } from "react";

export const useEvent = <T extends (...args: any[]) => any>(callback: T) => {
    const callbackRef = useRef(callback);

    useLayoutEffect(() => {
        callbackRef.current = callback;
    }, [callback]);

    const eventCallback = useCallback(
        (...args: Parameters<T>) => {
            return callbackRef.current.apply(null, args);
        },
        [callbackRef]
    );

    return eventCallback;
};
