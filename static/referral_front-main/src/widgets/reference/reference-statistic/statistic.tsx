import { Section } from "@/shared/ui/section";

import DashboardSprite from "@/assets/img/svg/dashboard-sprite.svg";

import { useFetchReferenceStatisticQuery } from "@/entities/reference/api";
import { Fetch } from "@/shared/ui/fetch";

const statistics = [
    { id: 1, label: "Всего кликов", key: "all_click", icon: "pie_chart" },
    { id: 2, label: "Регситраций", key: "register_count", icon: "bar_chart" },
    { id: 3, label: "Депозиты", key: "deposit", icon: "fluent_money_model_2" },
    { id: 4, label: "FTD's", key: "ftd_count", icon: "money_deposit" },
    { id: 5, label: "Вывод", key: "ftd_sum", icon: "fluent_money_model_1" },
    { id: 6, label: "P/L трейдеров", key: "witdraw_ref", icon: "scan_focus" },
    { id: 7, label: "Оборот", key: "oborot", icon: "money_exchange" }
];

export const ReferenceStatistic = () => {
    return (
        <Section>
            <Fetch
                useQuery={useFetchReferenceStatisticQuery}
                args={undefined}
                renderSuccess={data => (
                    <ul className="grid grid-cols-2 gap-4 lg:grid-cols-3 2xl:grid-cols-7">
                        {statistics.map(stats => (
                            <li
                                key={stats.id}
                                className="grid grid-cols-2 gap-y-3 rounded-2xl bg-[#2b2930] px-4 py-3 @container first:bg-violet-primary [&:nth-child(2)]:bg-violet-secondary"
                            >
                                <h2 className="col-span-2 row-start-3 text-sm/none @[15rem]:row-start-1 @[15rem]:text-lg/none">
                                    {stats.label}
                                </h2>

                                <svg
                                    width="45"
                                    height="45"
                                >
                                    <use
                                        xlinkHref={`${DashboardSprite}#${stats.icon}`}
                                    />
                                </svg>
                                <span className="col-span-2 mt-4 self-center text-2xl leading-none @[15rem]:col-span-1 @[15rem]:mt-0 @[15rem]:text-3xl">
                                    {data?.[stats.key]} $
                                </span>
                            </li>
                        ))}
                    </ul>
                )}
            />
        </Section>
    );
};
