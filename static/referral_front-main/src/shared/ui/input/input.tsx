import { inputVariants, type InputVariants } from "./input-variants";

interface InputProps extends React.ComponentProps<"input">, InputVariants {}

export const Input: React.FC<InputProps> = ({
    variant,
    className,
    autoComplete = "off",
    ...props
}) => {
    return (
        <input
            autoComplete={autoComplete}
            className={inputVariants({ variant, className })}
            {...props}
        />
    );
};
