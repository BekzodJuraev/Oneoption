import { useId } from "react";

import { Dialog } from "@/shared/ui/dialog";
import { Input } from "@/shared/ui/input/input";
import { Button, buttonVariants } from "@/shared/ui/button";
import { Title } from "@/shared/ui/title";

export const AddWalletForm = () => {
    const formId = `form-${useId()}`;

    return (
        <Dialog.Content className="space-y-8 rounded-2xl bg-[#141218] px-8 pb-8 pt-4">
            <Title as="h2">Добавление кошелька</Title>

            <form id={formId}>
                <label>
                    <span>Выберите тип кошелька:</span>
                    <Input placeholder="Выберите тип кошелька" />
                </label>

                <label>
                    <span>Кошелек:</span>
                    <Input placeholder="Введите ID кошелька" />
                </label>
            </form>

            <footer className="flex justify-end gap-x-5">
                <Dialog.Close
                    className={buttonVariants({
                        variant: "outlined",
                        className: "basis-60"
                    })}
                >
                    Отмена
                </Dialog.Close>
                <Button
                    form={formId}
                    className="basis-60"
                >
                    Добавить
                </Button>
            </footer>
        </Dialog.Content>
    );
};
