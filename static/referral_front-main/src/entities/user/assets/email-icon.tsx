interface EmailIconProps extends React.ComponentProps<"svg"> {}

export const EmailIcon: React.FC<EmailIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="0 0 34 34"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M5.66732 28.3333C4.88815 28.3333 4.22137 28.0561 3.66698 27.5017C3.1126 26.9474 2.83493 26.2801 2.83398 25.5V8.49999C2.83398 7.72082 3.11165 7.05405 3.66698 6.49966C4.22232 5.94527 4.8891 5.6676 5.66732 5.66666H28.334C29.1131 5.66666 29.7804 5.94432 30.3357 6.49966C30.8911 7.05499 31.1683 7.72177 31.1673 8.49999V25.5C31.1673 26.2792 30.8901 26.9464 30.3357 27.5017C29.7813 28.0571 29.1141 28.3343 28.334 28.3333H5.66732ZM17.0007 18.4167L5.66732 11.3333V25.5H28.334V11.3333L17.0007 18.4167ZM17.0007 15.5833L28.334 8.49999H5.66732L17.0007 15.5833ZM5.66732 11.3333V8.49999V25.5V11.3333Z"
                fill="currentColor"
            />
        </svg>
    );
};
