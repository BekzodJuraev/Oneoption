import { cn } from "@/shared/lib/utils/tailwind-merge";

interface SectionProps extends React.ComponentProps<"section"> {}

export const Section: React.FC<SectionProps> = ({ className, ...props }) => {
    return (
        <section
            className={cn(
                "rounded-2xl bg-secondary px-4-6-xs-md py-4 ",
                className
            )}
            {...props}
        />
    );
};
