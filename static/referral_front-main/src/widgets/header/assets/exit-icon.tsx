interface ExitIconProps extends React.ComponentProps<"svg"> {}

export const ExitIcon: React.FC<ExitIconProps> = props => {
    return (
        <svg
            width="1em"
            height="1em"
            viewBox="9 8 36 37"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}
        >
            <path
                d="M20.25 40.5L13.5 40.5L13.5 13.5L20.25 13.5L20.25 9L13.5 9C11.025 9 9 11.025 9 13.5L9 40.5C9 42.975 11.025 45 13.5 45L20.25 45L20.25 40.5ZM33.75 15.75L30.5775 18.9225L36.3825 24.75L18 24.75L18 29.25L36.3825 29.25L30.5775 35.0775L33.75 38.25L45 27L33.75 15.75Z"
                fill="currentColor"
            />
        </svg>
    );
};
