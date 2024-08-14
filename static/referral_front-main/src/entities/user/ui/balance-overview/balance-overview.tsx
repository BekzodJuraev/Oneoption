import { useFetchUserBalanceQuery } from "../../api";

import { Fetch } from "@/shared/ui/fetch";
import { Section } from "@/shared/ui/section";
import { Title } from "@/shared/ui/title";

import { BalanceOverviewList } from "./balance-overview-list";
import { BalanceOverviewListItem } from "./balance-overview-list-item";

const balance = [
    {
        id: 1,
        label: "Общий доход",
        key: "total_income"
    },
    {
        id: 2,
        label: "Доля от оборота",
        key: "income_oborot"
    },
    {
        id: 3,
        label: "Доля от дохода",
        key: "income_doxod"
    }
];

export const BalanceOverview = () => {
    return (
        <Section className="space-y-4">
            <Title as="h2">Ваш баланс</Title>

            <Fetch
                useQuery={useFetchUserBalanceQuery}
                args={undefined}
                renderSuccess={data => (
                    <BalanceOverviewList>
                        {balance.map(value => (
                            <BalanceOverviewListItem
                                key={value.id}
                                label={value.label}
                                value={data[value.key]}
                            />
                        ))}
                    </BalanceOverviewList>
                )}
            />
        </Section>
    );
};
