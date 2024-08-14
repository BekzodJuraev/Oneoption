import { Link, useNavigate } from "react-router-dom";

import { cn } from "@/shared/lib";

import { useSignOutMutation } from "@/shared/api";

interface SignOutButtonProps extends React.ComponentPropsWithoutRef<"a"> {}

export const SignOutButton: React.FC<SignOutButtonProps> = ({
    className,
    children,
    ...props
}) => {
    const navigate = useNavigate();
    const [signOut] = useSignOutMutation();

    const onClickHandler: React.MouseEventHandler<
        HTMLAnchorElement
    > = async event => {
        event.preventDefault();

        try {
            await signOut().unwrap();
            navigate("/");
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <Link
            to="/"
            onClick={onClickHandler}
            className={cn("flex h-full items-center justify-center", className)}
            {...props}
        >
            {children}
            <span className="sr-only">Logout</span>
        </Link>
    );
};
