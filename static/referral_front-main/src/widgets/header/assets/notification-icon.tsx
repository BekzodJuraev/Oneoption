interface NotificationIconProps extends React.ComponentProps<"svg"> {}

export const NotificationIcon: React.FC<NotificationIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="0 2 30 30"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M27.5003 23.2279C26.379 22.0115 24.281 20.1816 24.281 14.1875C24.281 9.63477 21.1193 5.99023 16.856 5.09609V3.875C16.856 2.83965 16.0249 2 15 2C13.9751 2 13.144 2.83965 13.144 3.875V5.09609C8.88073 5.99023 5.71896 9.63477 5.71896 14.1875C5.71896 20.1816 3.62097 22.0115 2.49973 23.2279C2.15151 23.6059 1.99714 24.0576 2.00004 24.5C2.00642 25.4609 2.75334 26.375 3.86298 26.375H26.137C27.2467 26.375 27.9942 25.4609 28 24.5C28.0029 24.0576 27.8485 23.6053 27.5003 23.2279ZM5.91918 23.5625C7.15069 21.9236 8.49712 19.2072 8.5035 14.2215C8.5035 14.2098 8.50002 14.1992 8.50002 14.1875C8.50002 10.5629 11.4099 7.625 15 7.625C18.5901 7.625 21.5 10.5629 21.5 14.1875C21.5 14.1992 21.4965 14.2098 21.4965 14.2215C21.5029 19.2078 22.8493 21.9242 24.0808 23.5625H5.91918ZM15 32C17.0498 32 18.7125 30.3213 18.7125 28.25H11.2875C11.2875 30.3213 12.9502 32 15 32Z"
                fill="currentColor"
            />
        </svg>
    );
};