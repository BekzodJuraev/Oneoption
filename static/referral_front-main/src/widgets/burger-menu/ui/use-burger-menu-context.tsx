import React, { createContext, useContext } from "react";

export const BurgerMenuContext = createContext<{
    burgerMenuTriggerId: string;
    burgerMenuId: string;
    triggerRef: React.RefObject<HTMLButtonElement>;
    currentFocusableElementIndex: React.RefObject<number>;
    dialogRef: React.RefObject<HTMLDialogElement>;
} | null>(null);

export const useBurgerMenuContext = () => {
    const context = useContext(BurgerMenuContext);

    if (!context) {
        throw new Error(
            "Component must be rendered as child of dialog component"
        );
    }

    return context;
};
