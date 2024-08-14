import { Input } from "@/shared/ui/input/input";
import { Button } from "@/shared/ui/button";

interface CashOutFormProps extends React.ComponentProps<"form"> {}

export const CashOutForm: React.FC<CashOutFormProps> = props => {
    return (
        <form
            {...props}
            className="grid gap-y-4"
        >
            <label className="grid gap-y-2">
                <span>Сумма</span>
                <Input
                    inputMode="numeric"
                    placeholder="Введите сумму в долларах США"
                />
            </label>

            <label className="grid gap-y-2">
                <span>Кошелек</span>
                <select className="h-11 rounded-lg bg-quaternary px-4 outline-offset-2 outline-slate-100 focus-visible:outline">
                    <option value="">Опция 1</option>
                    <option value="">Опция 2</option>
                    <option value="">Опция 3</option>
                </select>
            </label>

            <Button className="ml-auto mt-4 block">Вывести</Button>
        </form>
    );
};
