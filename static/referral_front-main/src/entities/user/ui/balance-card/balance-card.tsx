import { useFetchUserBalanceQuery } from "@/entities/user/api";

import { Section } from "@/shared/ui/section";
import { Button } from "@/shared/ui/button";

export const UserBalanceCard = () => {
    const { data: balance } = useFetchUserBalanceQuery();

    return (
        <Section className="flex flex-col gap-y-2 bg-violet-primary md:px-4">
            <h2 className="text-2xl">Ваш баланс</h2>
            <div className="mt-2 rounded-lg bg-violet-secondary px-4 py-2 text-lg">
                <p className="font-secondary">Общий доход:</p>
                <p className="py-4 text-center text-3xl">
                    {balance?.total_income}$
                </p>
            </div>
            <div className="rounded-lg bg-violet-secondary px-4 py-2 text-lg">
                <p>
                    <span className="font-secondary">Доля от дохода:</span>{" "}
                    {balance?.income_doxod} $
                </p>
            </div>

            <div className="rounded-lg bg-violet-secondary px-4 py-2 text-lg">
                <p>
                    <span className="font-secondary">Доля от оборота:</span>{" "}
                    {balance?.income_oborot} $
                </p>
            </div>

            <p className="mt-2 text-center">Обновляется каждые 10-20 минут.</p>
            <p className="text-center">
                Привлекайте новых трейдеров и увеличивайте доход!
            </p>

            <Button className="mx-auto mt-4 block h-auto bg-violet-tertiary">
                Перейти к выводу средств
            </Button>
        </Section>
    );
};
