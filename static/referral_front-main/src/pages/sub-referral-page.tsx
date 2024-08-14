import { Article } from "@/shared/ui/article";
import { Section } from "@/shared/ui/section";
import { ClipboardCopy } from "@/shared/ui/clipboard-copy";
import { Title } from "@/shared/ui/title";

export const SubReferralPage = () => {
    return (
        <Article
            variant="grid"
            className="md:grid-cols-2"
        >
            <Section className="space-y-4 @container">
                <Title
                    as="h2"
                    className="text-xl-2xl-xs-sm"
                >
                    Ссылка для привлечения партнеров
                </Title>

                <ClipboardCopy textToCopy="https//referal.link/nameadminname" />

                <p className="font-secondary text-base-lg-xs-md">
                    Привлекайте других партнеров в нашу партнерскую программу. И
                    получайте % от их заработка. Подробнее на странице
                    Партнерские программы. Ниже выводится статистика по
                    привлеченным партнерам. Обновляется раз в неделю.
                </p>
            </Section>

            <Section className="@container">
                <Title
                    as="h2"
                    className="text-xl-2xl-xs-sm"
                >
                    Комиссионные{" "}
                </Title>
            </Section>
        </Article>
    );
};
