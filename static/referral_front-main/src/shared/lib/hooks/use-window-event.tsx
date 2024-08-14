import { useEffect } from "react";

import { useEvent } from "./use-event";

type GetWindowEvent<Type extends string> = Type extends keyof WindowEventMap
    ? WindowEventMap[Type]
    : Event;

export function useWindowEvent<Type extends string>(
    type: Type,
    callback: (event: GetWindowEvent<Type>) => void,
    options?: AddEventListenerOptions
): void;

export function useWindowEvent(
    type: string,
    callback: (event: Event) => void,
    options?: AddEventListenerOptions
) {
    const eventCallback = useEvent(callback);

    useEffect(() => {
        document.addEventListener(type, eventCallback, options);

        return () => document.removeEventListener(type, eventCallback, options);
    }, [type, eventCallback, options]);
}
