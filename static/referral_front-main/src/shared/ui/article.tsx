import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "../lib/utils/tailwind-merge";

const articleVariants = cva(
    "pb-8 *:px-[clamp(1rem,_0.8rem_+_0.85vw,_1.5rem)]",
    {
        variants: {
            variant: {
                block: "space-y-[clamp(1rem,_0.8rem_+_0.85vw,_1.5rem)]",
                // grid: "grid gap-4 sm:gap-5 lg:gap-6 "
                grid: "grid gap-[clamp(1rem,_0.8rem_+_0.85vw,_1.5rem)]"
            }
        },
        defaultVariants: {
            variant: "block"
        }
    }
);

interface ArticleProps
    extends React.ComponentProps<"article">,
        VariantProps<typeof articleVariants> {}

export const Article: React.FC<ArticleProps> = ({
    className,
    variant,
    ...props
}) => {
    return (
        <article
            className={cn(articleVariants({ variant, className }))}
            {...props}
        />
    );
};
