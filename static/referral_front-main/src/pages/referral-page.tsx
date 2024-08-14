import { Article } from "@/shared/ui/article";
import { Title } from "@/shared/ui/title";
import { ClipboardCopy } from "@/shared/ui/clipboard-copy";

export const ReferralPage = () => {
    return (
        <Article
            variant="grid"
            className="grid-cols-2"
        >
            <section className="col-span-2 space-y-4 rounded-2xl bg-secondary py-4">
                <Title as="h2">
                    Улучшенная Программа Бонусов за Приглашения!
                </Title>

                <p className="font-secondary text-base-lg-xs-lg">
                    Вот как работает наша улучшенная программа: Когда кто-то
                    зарегистрируется по вашей рекомендации и совершит свой
                    первый депозит, вы повышаете бонусный уревень. Размер бонуса
                    зависит от количества приглашенных вами друзей:
                </p>
            </section>

            <section className="col-span-2 grid space-y-6 rounded-2xl bg-secondary py-4 @container md:col-span-1">
                <Title
                    as="h2"
                    className="text-lg-xl-xs-sm"
                >
                    Пригласите по реферальной ссылке и получите процент от
                    оборота:
                </Title>

                <ul className="grid auto-rows-[minmax(100px,_1fr)] grid-cols-[repeat(auto-fit,_minmax(250px,_1fr))] gap-4">
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">2% от оборота</strong>
                            <br />
                            <span>0 - 49 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">3% от оборота</strong>
                            <br />
                            <span>50 - 99 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">4% от оборота</strong>
                            <br />
                            <span>100 - 199 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">5% от оборота</strong>
                            <br />
                            <span>200 - 250 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">7% от оборота</strong>
                            <br />
                            <span>более 300 пополнений</span>
                        </p>
                    </li>
                </ul>

                <ClipboardCopy textToCopy="https//referal.link/nameadminname" />
            </section>

            <section className="col-span-2 grid space-y-6 rounded-2xl bg-secondary py-4 @container md:col-span-1">
                <Title
                    as="h2"
                    className="text-lg-xl-xs-sm"
                >
                    Пригласите по реферальной ссылке и заработайте долю от
                    дохода:
                </Title>

                <ul className="grid auto-rows-[minmax(100px,_1fr)] grid-cols-[repeat(auto-fit,_minmax(250px,_1fr))] gap-4">
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">40% от дохода</strong>
                            <br />
                            <span>0 - 49 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">50% от дохода</strong>
                            <br />
                            <span>50 - 99 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">60% от дохода</strong>
                            <br />
                            <span>100 - 199 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">70% от дохода</strong>
                            <br />
                            <span>200 - 250 первый депозитов</span>
                        </p>
                    </li>
                    <li className="flex min-h-24 items-center justify-center rounded-[1.25rem] bg-violet-primary px-4 py-3">
                        <p className="text-center">
                            <strong className="text-xl">80% от дохода</strong>
                            <br />
                            <span>более 300 пополнений</span>
                        </p>
                    </li>
                </ul>

                <ClipboardCopy textToCopy="https//referal.link/nameadminname" />
            </section>

            <footer className="col-span-2">
                Выводы реферальных счетов доступны толька по Понедельникам
            </footer>
        </Article>
    );
};

// const StyledSection = styled.section`
//     display: grid;
//     grid-template-columns: repeat(2, minmax(0, 1fr));
//     gap: 1rem;

//     @media (max-width: 768px) {
//         grid-template-columns: minmax(0, 1fr);
//     }
// `;

// const StyledList = styled.ul`
//     margin-top: 1.5rem;
//     list-style-type: none;
//     display: grid;
//     grid-template-columns: repeat(3, minmax(0, 1fr));
//     gap: 1rem;
// `;

// const StyledContainer = styled(Section).attrs({ as: "div" })`
//     container-type: inline-size;

//     @container (max-width: 650px) {
//         ${StyledList} {
//             /* background-color: #ffffff; */
//             grid-template-columns: repeat(2, minmax(0, 1fr));
//         }
//     }

//     @container (max-width: 425px) {
//         ${StyledList} {
//             /* background-color: #ffffff; */
//             grid-template-columns: 1fr;
//         }
//     }
// `;
