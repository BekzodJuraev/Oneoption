import { useFetchReferenceChartDataQuery } from "@/entities/reference/api";
import { Fetch } from "@/shared/ui/fetch";

import { LineChart } from "@/shared/ui/line-chart";

export const ReferenceActivityChart = ({
    frequency
}: {
    frequency: "daily" | "weekly" | "monthly";
}) => {
    return (
        <Fetch
            useQuery={useFetchReferenceChartDataQuery}
            args={{ frequency: frequency }}
            renderSuccess={data => <LineChart data={data} />}
        />
    );
};
