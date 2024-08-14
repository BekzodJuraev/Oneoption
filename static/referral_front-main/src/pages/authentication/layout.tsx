import { Outlet } from "react-router-dom";
import { cnBase } from "tailwind-variants";

interface AuthenticationLayoutProps
    extends Omit<React.ComponentPropsWithoutRef<"main">, "children"> {}

export const AuthenticationLayout: React.FC<AuthenticationLayoutProps> = ({
    className,
    ...props
}) => {
    return (
        <main
            className={cnBase(
                "min-h-dvh bg-[url('@/assets/bg.webp')] px-4 py-8",
                className
            )}
            {...props}
        >
            <section className="mx-auto max-w-3xl space-y-6-8-xs-md">
                <Outlet />
            </section>
        </main>
    );
};
