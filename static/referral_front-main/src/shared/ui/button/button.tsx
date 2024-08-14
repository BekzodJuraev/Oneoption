import { buttonVariants, type ButtonVariants } from "./button-variants";

interface ButtonProps extends React.ComponentProps<"button">, ButtonVariants {}

export const Button: React.FC<ButtonProps> = ({
    variant,
    className,
    ...props
}) => {
    return (
        <button
            className={buttonVariants({ variant, className })}
            {...props}
        />
    );
};
