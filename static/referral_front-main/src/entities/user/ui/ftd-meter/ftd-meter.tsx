import "./index.css";

import { cn } from "@/shared/lib";

interface FTDMeterProps extends React.ComponentProps<"div"> {
    "aria-valuenow": number;
    "aria-valuemax": number;
}

export const FTDMeter: React.FC<FTDMeterProps> = ({ className, ...props }) => {
    return (
        <div
            role="meter"
            style={{
                "--start": `${Math.round((props["aria-valuenow"] / props["aria-valuemax"]) * 100)}%`
            }}
            className={cn("meter", className)}
            {...props}
        >
            FTD {props["aria-valuenow"]} / {props["aria-valuemax"]}
        </div>
    );
};
