import { tv, type VariantProps } from "tailwind-variants";

export const buttonVariants = tv({
    base: "rounded-lg border border-violet-primary select-none",
    variants: {
        variant: {
            primary: "bg-violet-primary px-10 py-2.5",
            outlined: "bg-transparent px-10 py-2.5"
        }
    },
    defaultVariants: {
        variant: "primary"
    }
});

export type ButtonVariants = VariantProps<typeof buttonVariants>;
