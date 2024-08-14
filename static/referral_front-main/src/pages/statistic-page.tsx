import { BalanceOverview } from "@/entities/user/ui/balance-overview";

import { Section } from "@/shared/ui/section";
import { Table } from "@/shared/ui/table";
import { LineChart } from "@/shared/ui/line-chart";
import { SearchForm, SearchFormFields } from "@/shared/ui/search-form";
import { Article } from "@/shared/ui/article";
import { Title } from "@/shared/ui/title";

const data = Array(6).fill({
    number: 1,
    nick: "Ник",
    id: 3621548,
    as: "70%",
    asd: "231 $",
    fds: "378 $",
    gdf: "571 $",
    gdfd: "572 $",
    gdfg: "573 $"
});

export const StatisticPage = () => {
    const onSearchHandler: React.FormEventHandler<
        HTMLFormElement & SearchFormFields
    > = event => {
        event.preventDefault();

        const { query } = event.currentTarget;

        console.log(query.value);
    };

    return (
        <Article>
            <Section>
                <LineChart
                    data={[
                        [1, 1],
                        [2, 2]
                    ]}
                />
            </Section>

            {/* <Section className="space-y-4">
                <Title as="h2">Ваш баланс</Title>

                <ul className="grid gap-3 sm:grid-cols-3 md:gap-4 lg:gap-6">
                    <li className="grid grid-cols-2 grid-rows-2 rounded-xl bg-violet-primary px-3-4-xs-md py-3">
                        <h3 className="col-span-2 text-sm-base-xs-lg">
                            Общий доход
                        </h3>
                        <strong className="col-span-2 justify-self-center text-2xl-3xl-xs-lg lg:col-start-2">
                            0,00 $
                        </strong>
                    </li>

                    <li className="grid grid-cols-2 grid-rows-2 rounded-xl bg-tertiary px-3-4-xs-md py-3">
                        <h3 className="col-span-2 text-sm-base-xs-lg">
                            Доля от оборота
                        </h3>
                        <strong className="col-span-2 justify-self-center text-2xl-3xl-xs-lg lg:col-start-2">
                            0,00 $
                        </strong>
                    </li>

                    <li className="grid grid-cols-2 grid-rows-2 rounded-xl bg-tertiary px-3-4-xs-md py-3">
                        <h3 className="col-span-2 text-sm-base-xs-lg">
                            Доля от дохода
                        </h3>
                        <strong className="col-span-2 justify-self-center text-2xl-3xl-xs-lg lg:col-start-2">
                            0,00 $
                        </strong>
                    </li>
                </ul>
            </Section> */}
            <BalanceOverview />

            <Section>
                <header className="grid grid-cols-1 gap-x-4 gap-y-2 sm:grid-cols-2">
                    <Title
                        as="h2"
                        className="whitespace-nowrap text-lg-xl-xs-lg"
                    >
                        Таблица рефералов
                    </Title>
                    <SearchForm
                        className="justify-self-end sm:max-w-none sm:justify-self-stretch"
                        onSubmit={onSearchHandler}
                    />
                </header>
                <div className="scrollbar">
                    <Table
                        headers={[
                            "#",
                            "Никнейм",
                            "ID",
                            "Доходность",
                            "Оборот",
                            "Депозиты",
                            "Выводы",
                            "Баланс",
                            "Прибыль"
                        ]}
                        data={data}
                    />
                </div>
            </Section>
        </Article>
    );
};
