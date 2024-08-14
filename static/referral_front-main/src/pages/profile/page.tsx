import { useId } from "react";

import { UpdateUserPhotoForm } from "@/features/user/update-avatar";

import { ChangePasswordForm } from "@/entities/user/ui/forms/change-password-form";

import { UserBalanceCard } from "@/entities/user/ui/balance-card";

import { Dialog } from "@/shared/ui/dialog";
import { Article } from "@/shared/ui/article";
import { Section } from "@/shared/ui/section";
import { Button } from "@/shared/ui/button";

import { UserFTDMeter } from "@/entities/user/ui/ftd-meter";
import { Table, TableRow } from "@/shared/ui/table";
import * as Tooltip from "@/shared/ui/tooltip";

// import Avatar from "@/assets/avatar.png";

import TelegramLogo from "@/assets/img/telegram-logo.png";
import InstagramLogo from "@/assets/img/instagram-logo.png";
import YouTubeLogo from "@/assets/img/youtube-logo.png";
import { AddWalletForm } from "@/features/wallet/add";

const tooltipData = {
    level: 1,
    revenue: 40,
    turnover: 2,
    deposit: "0 - 50"
} as const;

export const ProfilePage = () => {
    const formId = useId();

    return (
        <Article
            variant="grid"
            className="lg:grid-cols-[minmax(0,_3fr)_minmax(0,_4fr)_minmax(0,_4fr)]"
        >
            <Section
                className="flex flex-col items-center gap-y-2 overflow-hidden pb-0 text-center md:px-4"
                // className="space-y-4 pb-0"
            >
                <header className="self-start text-2xl">
                    <h2>
                        LVL <strong className="text-violet-primary">1</strong>{" "}
                        <Tooltip.Root>
                            <Tooltip.Trigger>
                                <a>
                                    <svg
                                        width="14"
                                        height="14"
                                        viewBox="0 0 14 14"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="mb-0.5 inline-block cursor-help"
                                    >
                                        <path
                                            d="M14 7C14 10.866 10.866 14 7 14C3.13401 14 0 10.866 0 7C0 3.13401 3.13401 0 7 0C10.866 0 14 3.13401 14 7Z"
                                            fill="#555555"
                                        />
                                        <path
                                            d="M6.11111 5H6.55556L7.88889 5.84V11H6.11111V5ZM6 3.044V2.9C6 2.408 6.21111 2 6.95556 2H7.04444C7.78889 2 8 2.408 8 2.9V3.044C8 3.536 7.78889 3.944 7.04444 3.944H6.95556C6.21111 3.944 6 3.536 6 3.044Z"
                                            fill="white"
                                        />
                                    </svg>
                                </a>
                            </Tooltip.Trigger>
                            <Tooltip.Portal>
                                <Tooltip.Content className="z-50 max-w-[calc(100dvw_-_2rem)] rounded-xl border-2 border-violet-primary bg-[#211F26] shadow-md">
                                    <section className="px-4 pt-2 text-white">
                                        <header>
                                            <h3 className="font-primary text-xl">
                                                Уровень партнера
                                            </h3>
                                            <p className="mt-2 text-base">
                                                Увеличивай число депозитов и
                                                получай больше прибыли !
                                            </p>
                                        </header>
                                        <Table
                                            uniqueKey="id"
                                            headers={[
                                                "Уровень",
                                                "Доход",
                                                "Оборот",
                                                "Депозит"
                                            ]}
                                            data={Array(5).fill(tooltipData)}
                                            renderHeader={headers => (
                                                <thead>
                                                    <TableRow>
                                                        {headers.map(
                                                            (header, i) => (
                                                                <th
                                                                    key={i}
                                                                    className="bg-[#36343B] px-3 py-1.5 text-sm font-normal normal-case"
                                                                >
                                                                    {header}
                                                                </th>
                                                            )
                                                        )}
                                                    </TableRow>
                                                </thead>
                                            )}
                                            renderData={data => (
                                                <tbody className="text-center">
                                                    {data.map((row, i) => (
                                                        <tr
                                                            key={i}
                                                            className="bg-[#4A484F] first:bg-violet-primary"
                                                        >
                                                            {Object.values(
                                                                row
                                                            ).map((cell, j) => (
                                                                <td
                                                                    key={j}
                                                                    className="px-3 py-1.5"
                                                                >
                                                                    {cell}
                                                                </td>
                                                            ))}
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            )}
                                            className="mt-2 border-separate border-spacing-x-0 border-spacing-y-0.5 rounded-lg shadow-lg"
                                        />

                                        <footer className="-mx-4 mt-2 rounded-b-xl bg-violet-primary py-2.5 text-center">
                                            <p className="font-primary text-xl/none">
                                                FTD 26 / 99
                                            </p>
                                            <p>до следующего уровня</p>
                                        </footer>
                                    </section>
                                </Tooltip.Content>
                            </Tooltip.Portal>
                        </Tooltip.Root>
                    </h2>
                </header>

                {/* <img
                    src={Avatar}
                    alt=""
                    className="width-48 aspect-square rounded-full border-4 border-violet-primary"
                /> */}

                <UpdateUserPhotoForm />

                <h3 className="w-full truncate text-4xl">vikhlyaevvik</h3>
                <p className="w-full truncate font-secondary text-2xl">
                    vikhlyaevvik@yandex.ru
                </p>

                <div className="my-2 w-full rounded-xl bg-quaternary px-2.5 py-1.5 font-secondary text-lg">
                    <p className="text-start">Привлечение реферралов из:</p>

                    <ul className="mt-3 flex gap-x-2">
                        <li className="flex size-12 items-center justify-center rounded-lg bg-[#2b2930]">
                            <img
                                src={TelegramLogo}
                                alt=""
                            />
                        </li>
                        <li className="flex size-12 items-center justify-center rounded-lg bg-[#2b2930]">
                            <img
                                src={InstagramLogo}
                                alt=""
                            />
                        </li>
                        <li className="flex size-12 items-center justify-center rounded-lg bg-[#2b2930]">
                            <img
                                src={YouTubeLogo}
                                alt=""
                            />
                        </li>
                    </ul>
                </div>

                <footer className="-mx-6 mt-auto h-9 w-[calc(100%_+_3rem)] rounded-b-2xl text-center leading-9">
                    <UserFTDMeter
                        aria-valuenow={30}
                        aria-valuemax={99}
                    />
                </footer>
            </Section>

            <UserBalanceCard />

            <Section className="grid grid-rows-[auto_auto_1fr] gap-y-4 md:px-4">
                <h2 className="text-2xl">Безопасность</h2>

                <ChangePasswordForm id={formId} />

                <Button
                    form={formId}
                    className="h-11 lg:self-end lg:justify-self-end"
                >
                    Сменить пароль
                </Button>
            </Section>

            <Section className="lg:col-span-3">
                <header className="flex justify-between">
                    <h2>Кошельки</h2>
                    <Dialog.Root>
                        <Dialog.Trigger className="rounded-lg bg-violet-primary px-10 py-2.5">
                            Добавить
                        </Dialog.Trigger>

                        <Dialog.Portal>
                            <AddWalletForm />
                        </Dialog.Portal>
                    </Dialog.Root>
                </header>
            </Section>
        </Article>
    );
};
