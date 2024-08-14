import { createContext, useContext } from "react";

export const DialogContext = createContext<{
    dialogId: string;
    dialogRef: React.RefObject<HTMLDialogElement>;
    triggerRef: React.RefObject<HTMLButtonElement>;
} | null>(null);

export const useDialogContext = () => {
    const context = useContext(DialogContext);

    if (!context) {
        throw new Error(
            "Component must be rendered as child of Dialog component"
        );
    }

    return context;
};
