interface StatisticIconProps extends React.ComponentProps<"svg"> {}

export const StatisticIcon: React.FC<StatisticIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M7 22C6.44772 22 6 22.4477 6 23V25C6 25.5523 6.44772 26 7 26H9C9.55228 26 10 25.5523 10 25V23C10 22.4477 9.55228 22 9 22H7Z"
                fill="currentColor"
            />
            <path
                d="M14 23C14 22.4477 14.4477 22 15 22H17C17.5523 22 18 22.4477 18 23V25C18 25.5523 17.5523 26 17 26H15C14.4477 26 14 25.5523 14 25V23Z"
                fill="currentColor"
            />
            <path
                d="M23 22C22.4477 22 22 22.4477 22 23V25C22 25.5523 22.4477 26 23 26H25C25.5523 26 26 25.5523 26 25V23C26 22.4477 25.5523 22 25 22H23Z"
                fill="currentColor"
            />
            <path
                d="M28 2C30.2091 2 32 3.79086 32 6V26C32 28.2091 30.2091 30 28 30H4C1.79086 30 0 28.2091 0 26V6C0 3.79086 1.79086 2 4 2H28ZM4 28H28C29.1046 28 30 27.1046 30 26V10H2V26C2 27.1046 2.89543 28 4 28ZM4 4C2.89543 4 2 4.89543 2 6V8H30V6C30 4.89543 29.1046 4 28 4H4Z"
                fill="currentColor"
            />
        </svg>
    );
};
