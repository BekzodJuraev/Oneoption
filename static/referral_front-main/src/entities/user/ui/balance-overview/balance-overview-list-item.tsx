import { cnBase } from "tailwind-variants";

interface BalanceOverviewListItemProps
    extends Omit<React.ComponentPropsWithoutRef<"li">, "children"> {
    label: string;
    value: string;
}

export const BalanceOverviewListItem: React.FC<
    BalanceOverviewListItemProps
> = ({ label, value, className, ...props }) => {
    return (
        <li
            className={cnBase(
                "rounded-xl bg-tertiary px-3-4-xs-md py-3 first-of-type:bg-violet-primary",
                className
            )}
            {...props}
        >
            <dl className="grid grid-cols-2 grid-rows-2">
                <dt className="col-span-2 text-sm-base-xs-lg">{label}</dt>
                <dd className="col-span-2 justify-self-center text-2xl-3xl-xs-lg lg:col-start-2">
                    {value} $
                </dd>
            </dl>
        </li>
    );
};
