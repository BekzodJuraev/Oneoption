import { CashOutForm } from "@/entities/user/ui/forms/cash-out-form";
import { Article } from "@/shared/ui/article";
import { Section } from "@/shared/ui/section";

export const CashOutPage = () => {
    return (
        <Article
            variant="grid"
            className="lg:grid-cols-[minmax(0,_1fr)_minmax(0,_2fr)]"
        >
            <Section className="space-y-6">
                <h2 className="text-xl-2xl-xs-lg">Вывод средств</h2>
                <CashOutForm />
            </Section>

            <Section className="space-y-6">
                <h2 className="text-xl-2xl-xs-lg">Часто задаваемые вопросы</h2>
                <ul className="space-y-4">
                    <li className="space-y-1">
                        <h3 className="text-lg-xl-xs-lg">
                            Что значит статус "Обработка"?
                        </h3>
                        <p className="font-secondary text-base-lg-xs-lg">
                            Средства отправлены финансовому провайдеру и ожидают
                            проводки на его стороне. Срок зачисления - до 3-х
                            суток. Ожидайте, пожалуйста. С нашей стороны мы
                            никак ускорить процесс не можем.
                        </p>
                    </li>
                    <li className="space-y-1">
                        <h3 className="text-lg-xl-xs-lg">
                            Статус сменился на "Завершен", но деньги не
                            поступили
                        </h3>
                        <p className="font-secondary text-base-lg-xs-lg">
                            Срок зачисления средств до 3-х суток. Ожидайте,
                            деньги придут. Если спустя 3-е суток средства не
                            поступили - напишите нам.
                        </p>
                    </li>
                    <li className="space-y-1">
                        <h3 className="text-lg-xl-xs-lg">
                            Деньги пришли не полностью
                        </h3>
                        <p className="font-secondary text-base-lg-xs-lg">
                            Вывод средств на карту может разбиваться на части,
                            части могут приходить в разное время. Не
                            переживайте, средства поступят. Если в течение 3-х
                            суток средства не поступили - обратитесь к нам.
                        </p>
                    </li>
                </ul>
            </Section>
        </Article>
    );
};
