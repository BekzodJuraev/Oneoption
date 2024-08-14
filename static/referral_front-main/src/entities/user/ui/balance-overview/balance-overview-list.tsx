import { cnBase } from "tailwind-variants";

interface BalanceOverviewListProps
    extends React.ComponentPropsWithoutRef<"ul"> {}

export const BalanceOverviewList: React.FC<BalanceOverviewListProps> = ({
    className,
    ...props
}) => {
    return (
        <ul
            className={cnBase(
                "grid gap-3 sm:grid-cols-3 md:gap-4 lg:gap-6",
                className
            )}
            {...props}
        />
    );
};
