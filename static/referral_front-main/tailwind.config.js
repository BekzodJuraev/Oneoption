import { withTV } from "tailwind-variants/transformer";
import containerPlugin from "@tailwindcss/container-queries";

/** @type {import('tailwindcss').Config} */
export default withTV({
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
                primary: "#141218",
                secondary: "#211F26",
                tertiary: "#28262D",
                quaternary: "#36343B",
                violet: {
                    primary: "#793aff",
                    secondary: "#4619a6",
                    tertiary: "#1f0060",
                    quaternary: "#652cde"
                },
                white: {
                    DEFAULT: "#ffffff",
                    primary: "#fef7ff"
                }
            },
            fontFamily: {
                primary: "GetVoIP Grotesque",
                secondary: "Jost"
            },
            padding: {
                "2-4-xs-md": "clamp(0.5rem, 0.05rem + 1.95cqi, 1rem)",
                "2-4-xs-lg": "clamp(0.5rem, 0.25rem + 1.2cqi, 1rem)",
                "3-4-xs-md": "clamp(0.75rem, 0.55rem + 1cqi, 1rem)",
                "4-6-xs-md": "clamp(1rem, 0.55rem + 1.95cqi, 1.5rem)",
                "4-6-xs-lg": "clamp(1rem, 0.75rem + 1.2cqi, 1.5rem)"
            },
            margin: {
                "2-3-xs-md": "clamp(0.5rem, 0.3rem + 1cqi, 0.75rem)"
            },
            spacing: {
                "2-3-xs-md": "clamp(0.5rem, 0.3rem + 1cqi, 0.75rem)",
                "6-8-xs-md": "clamp(1.5rem, 1.05rem + 1.95cqi, 2rem)"
            },
            size: {
                "6-8-xs-md": "clamp(1.5rem, 1.05rem + 1.95cqi, 2rem)"
            },
            gap: {
                "2-4-xs-md": "clamp(0.5rem, 0.05rem + 1.95cqi, 1rem)",
                "6-8-xs-md": "clamp(1.5rem, 1.05rem + 1.95cqi, 2rem)"
            },
            fontSize: {
                "xs-base-xs-lg": "clamp(0.75rem, 0.6rem + 0.6cqi, 1rem)",
                "sm-base-xs-lg": "clamp(0.875rem, 0.8rem + 0.3cqi, 1rem)",
                "sm-base-xs-sm": "clamp(0.875rem, 0.7rem + 0.715cqi, 1rem)",
                "sm-lg-xs-md": "clamp(0.875rem, 0.65rem + 1cqi, 1.125rem)",
                "base-lg-xs-md": "clamp(1rem, 0.85rem + 0.715cqi, 1.125rem)",
                "base-lg-xs-lg": "clamp(1rem, 0.95rem + 0.3cqi, 1.125rem)",
                "base-xl-xs-md": "clamp(1rem, 0.8rem + 1cqi, 1.25rem)",
                "lg-xl-xs-sm": "clamp(1.125rem, 0.95rem + 0.715cqi, 1.25rem)",
                "lg-xl-xs-lg": "clamp(1.125rem, 1.05rem + 0.3cqi, 1.25rem)",
                "xl-2xl-xs-sm": "clamp(1.25rem, 0.9rem + 1.5cqi, 1.5rem)",
                "xl-2xl-xs-md": "clamp(1.25rem, 1rem + 1cqi, 1.5rem)",
                "xl-2xl-xs-lg": "clamp(1.25rem, 1.1rem + 0.6cqi, 1.5rem)",
                "2xl-3xl-xs-lg": "clamp(1.5rem, 1.3rem + 0.9cqi, 1.875rem)",
                "2xl-3xl-md-xl": "clamp(1.5rem, 0.95rem + 1.175cqi, 1.875rem)",
                "xl-4xl-xs-md": "clamp(1.25rem, 0.35rem + 3.95cqi, 2.25rem)",
                "2xl-4xl-xs-md": "clamp(1.5rem, 0.85rem + 2.95cqi, 2.25rem)",
                "3xl-4xl-xs-lg": "clamp(1.875rem, 1.675rem + 0.9cqi, 2.25rem)",
                "4xl-6xl-xs-md": "clamp(2.25rem, 0.925rem + 5.875cqi, 3.75rem)",
                "4xl-7xl-xs-md": "clamp(2rem, 0.25rem + 7.85cqi, 4rem)"
            },
            screens: {
                xs: "360px",
                "2xs": "448px",
                "3xs": "512px",
                "4xs": "576px",
                "md-l": {
                    raw: "(orientation: landscape)"
                },
                mh: { raw: "(hover: hover)" }
            }
        }
    },
    corePlugins: {
        container: false
    },
    plugins: [containerPlugin]
});
