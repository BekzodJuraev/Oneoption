export const defaultTheme = {
    color: {
        black: {
            primary: "#1f1f1f", //? background page
            secondary: "#0a0a0a", //? background section
            tertiary: "#131313" //? background block
        },
        white: "#ffffff",
        lime: {
            primary: "#b8f802"
        },
        gray: {
            primary: "#636363"
        },
        transparent: "rgba(255, 255, 255, 0)"
    },
    "z-index": {
        1: "1", //? Для наползающих элементов в общем потоке
        2: "2", //? Для наползающих элементов в общем потоке
        3: "3", //? Для масок
        4: "4", //? Для сайдбаров
        5: "5", //? Для модалок
        6: "6" //? Для элементов, перекрывающих всё
    }
} as const;

export type ThemeType = typeof defaultTheme;

// Primary (первичный)
// Secondary (вторичный)
// Tertiary (третичный)
// Quaternary (четвертичный)
// Quinary (пятый)
// Senary (шестой)
// Septenary (седьмой)
// Octonary (восьмой)
// Nonary (девятый)
// Denary (десятый)
