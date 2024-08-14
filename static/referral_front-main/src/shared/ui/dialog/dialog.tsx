import { useRef, useId } from "react";

import { composeEventHandlers } from "@/shared/lib/utils/compose-event-handlers";

import { Portal as DialogPortal } from "../portal";
import { DialogContext, useDialogContext } from "./use-dialog-context";

import Dialog from "./Dialog.module.css";

interface RootProps extends React.PropsWithChildren {}

export const Root: React.FC<RootProps> = ({ children }) => {
    const dialogId = `dialog-${useId()}`;
    const dialogRef = useRef<HTMLDialogElement>(null);
    const triggerRef = useRef<HTMLButtonElement>(null);

    return (
        <DialogContext.Provider value={{ dialogId, dialogRef, triggerRef }}>
            {children}
        </DialogContext.Provider>
    );
};

Root.displayName = "Dialog.Root";

interface TriggerProps
    extends Omit<
        React.ComponentProps<"button">,
        "aria-haspopup" | "aria-controls"
    > {}

export const Trigger: React.FC<TriggerProps> = ({ onClick, ...props }) => {
    const { dialogId, dialogRef, triggerRef } = useDialogContext();

    const onClickHandler: React.MouseEventHandler<
        HTMLButtonElement
    > = event => {
        const trigger = event.currentTarget;
        const dialog = dialogRef.current;
        const dialogOpen = trigger.getAttribute("aria-expanded") === "true";

        if (dialogOpen) {
            dialog?.close();
        } else {
            dialog?.showModal();
        }

        trigger.setAttribute("aria-expanded", String(!dialogOpen));
    };

    return (
        <button
            aria-haspopup="dialog"
            aria-expanded="false"
            aria-controls={dialogId}
            onClick={composeEventHandlers(onClick, onClickHandler)}
            ref={triggerRef}
            {...props}
        />
    );
};

Trigger.displayName = "Dialog.Trigger";

interface PortalProps extends React.PropsWithChildren {}

export const Portal: React.FC<PortalProps> = ({ children }) => {
    return <DialogPortal>{children}</DialogPortal>;
};

Portal.displayName = "Dialog.Portal";

interface ContentProps extends React.ComponentProps<"dialog"> {}

export const Content: React.FC<ContentProps> = ({
    className,
    onClick,
    children,
    ...props
}) => {
    const { dialogRef, triggerRef } = useDialogContext();

    const handleOverlayClick: React.MouseEventHandler<
        HTMLDialogElement
    > = event => {
        if (event.target !== dialogRef.current) return;

        dialogRef.current?.close();
        triggerRef.current?.setAttribute("aria-expanded", "false");
    };

    return (
        <dialog
            className={Dialog.content}
            onClick={handleOverlayClick}
            ref={dialogRef}
            {...props}
        >
            <section
                className={className}
                onClick={onClick}
            >
                {children}
            </section>
        </dialog>
    );
};

Content.displayName = "Dialog.Content";

interface CloseProps
    extends Omit<
        React.ComponentProps<"button">,
        "aria-haspopup" | "aria-controls"
    > {}

export const Close: React.FC<CloseProps> = ({ onClick, ...props }) => {
    const { dialogRef, triggerRef } = useDialogContext();

    const onClickHandler: React.MouseEventHandler<HTMLButtonElement> = () => {
        const trigger = triggerRef.current;
        const dialog = dialogRef.current;

        dialog?.close();
        trigger?.setAttribute("aria-expanded", "false");
    };

    return (
        <button
            onClick={composeEventHandlers(onClick, onClickHandler)}
            {...props}
        />
    );
};

Close.displayName = "Dialog.Close";
