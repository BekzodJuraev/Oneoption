import {
    CashOutIcon,
    DashboardIcon,
    ExitIcon,
    NotificationIcon,
    PartnershipAgreementIcon,
    ProfileIcon,
    ReferralProgramIcon,
    StatisticIcon,
    SubReferralProgramIcon,
    SupportIcon,
    TelegramIcon
} from "../assets";

interface SVGPickerProps extends React.SVGAttributes<SVGSVGElement> {
    name:
        | "cash-out"
        | "dashboard"
        | "exit"
        | "notification"
        | "partnership-agreement"
        | "referral"
        | "statistic"
        | "sub-referral"
        | "support"
        | "profile"
        | "telegram";
}

export const SVGPicker: React.FC<SVGPickerProps> = ({ name, ...props }) => {
    switch (name) {
        case "cash-out":
            return <CashOutIcon {...props} />;

        case "dashboard":
            return <DashboardIcon {...props} />;

        case "exit":
            return <ExitIcon {...props} />;

        case "notification":
            return <NotificationIcon {...props} />;

        case "partnership-agreement":
            return <PartnershipAgreementIcon {...props} />;

        case "referral":
            return <ReferralProgramIcon {...props} />;

        case "sub-referral":
            return <SubReferralProgramIcon {...props} />;

        case "statistic":
            return <StatisticIcon {...props} />;

        case "profile":
            return <ProfileIcon {...props} />;

        case "support":
            return <SupportIcon {...props} />;

        case "telegram":
            return <TelegramIcon {...props} />;

        default:
            return null;
    }
};
