import { cnBase } from "tailwind-variants";

import Logo from "@/assets/logo.png";

interface AuthorizationHeaderProps
    extends React.ComponentPropsWithoutRef<"header"> {}

export const AuthorizationHeaderWidget: React.FC<AuthorizationHeaderProps> = ({
    className,
    children,
    ...props
}) => {
    return (
        <header
            className={cnBase("space-y-2-3-xs-md text-center", className)}
            {...props}
        >
            <img
                src={Logo}
                alt="Logo"
                height="125"
                width="220"
                className="mx-auto block"
            />
            {children}
        </header>
    );
};
