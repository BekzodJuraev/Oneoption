interface DashboardIconProps extends React.ComponentProps<"svg"> {}

export const DashboardIcon: React.FC<DashboardIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="0 0 36 36"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <rect
                width="16"
                height="16"
                fill="currentColor"
            />
            <rect
                x="20"
                width="16"
                height="16"
                fill="currentColor"
            />
            <rect
                x="20"
                y="20"
                width="16"
                height="16"
                fill="currentColor"
            />
            <rect
                y="20"
                width="16"
                height="16"
                fill="currentColor"
            />
        </svg>
    );
};
