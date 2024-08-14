import styles from "./index.module.css";

import { cn } from "@/shared/lib";

interface CheckboxProps extends Omit<React.ComponentProps<"input">, "type"> {}

export const Checkbox: React.FC<CheckboxProps> = ({ className, ...props }) => {
    return (
        <input
            type="checkbox"
            className={cn(styles.checkbox, className)}
            {...props}
        />
    );
};
