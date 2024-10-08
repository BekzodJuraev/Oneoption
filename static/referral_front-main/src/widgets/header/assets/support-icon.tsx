interface SupportIconProps extends React.ComponentProps<"svg"> {}

export const SupportIcon: React.FC<SupportIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="0 0 36 36"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M18 3C9.729 3 3 9.729 3 18V24.2145C3 25.7505 4.3455 27 6 27H7.5C7.89782 27 8.27936 26.842 8.56066 26.5607C8.84196 26.2794 9 25.8978 9 25.5V17.7855C9 17.3877 8.84196 17.0061 8.56066 16.7248C8.27936 16.4435 7.89782 16.2855 7.5 16.2855H6.138C6.972 10.4805 11.967 6 18 6C24.033 6 29.028 10.4805 29.862 16.2855H28.5C28.1022 16.2855 27.7206 16.4435 27.4393 16.7248C27.158 17.0061 27 17.3877 27 17.7855V27C27 28.6545 25.6545 30 24 30H21V28.5H15V33H24C27.309 33 30 30.309 30 27C31.6545 27 33 25.7505 33 24.2145V18C33 9.729 26.271 3 18 3Z"
                fill="currentColor"
            />
        </svg>
    );
};
