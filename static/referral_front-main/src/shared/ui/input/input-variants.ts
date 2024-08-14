import { tv, type VariantProps } from "tailwind-variants";

export const inputVariants = tv({
    variants: {
        variant: {
            primary:
                "h-11 w-full rounded-lg bg-quaternary px-4 outline-offset-2 outline-slate-100 placeholder:text-white/30 focus-visible:outline"
        }
    },
    defaultVariants: {
        variant: "primary"
    }
});

export type InputVariants = VariantProps<typeof inputVariants>;
