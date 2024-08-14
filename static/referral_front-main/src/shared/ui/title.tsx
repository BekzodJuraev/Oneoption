import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "../lib";

const titleVariants = cva("", {
    variants: {
        as: {
            h1: "text-2xl-3xl-xs-lg",
            h2: "text-xl-2xl-xs-lg"
        }
    },
    defaultVariants: {
        as: "h1"
    }
});

interface TitleProps
    extends React.ComponentProps<"h1">,
        VariantProps<typeof titleVariants> {}

export const Title: React.FC<TitleProps> = ({
    as: Element = "h1",
    className,
    ...props
}) => {
    return (
        <Element
            className={cn(titleVariants({ as: Element, className }))}
            {...props}
        />
    );
};
