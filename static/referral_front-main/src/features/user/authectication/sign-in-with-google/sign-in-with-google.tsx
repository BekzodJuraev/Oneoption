import { cnBase } from "tailwind-variants";

import { useLazySignInWithGoogleQuery } from "@/shared/api";

import { composeEventHandlers } from "@/shared/lib/utils/compose-event-handlers";

interface SignInWithGoogle extends React.ComponentPropsWithoutRef<"button"> {}

export const SignInWithGoogle: React.FC<SignInWithGoogle> = ({
    className,
    onClick,
    ...props
}) => {
    const [signInWithGoogle] = useLazySignInWithGoogleQuery();

    const authenticateWithGoogle: React.MouseEventHandler<
        HTMLButtonElement
    > = async () => {
        try {
            await signInWithGoogle();
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <button
            onClick={composeEventHandlers(onClick, authenticateWithGoogle)}
            className={cnBase(
                "rounded-lg border-2 border-white-primary py-3 transition-colors duration-300 sm:px-16 mh:hover:bg-white-primary mh:hover:text-black",
                className
            )}
            {...props}
        >
            Войти через Google
        </button>
    );
};
