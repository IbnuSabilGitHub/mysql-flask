/** @type {import('tailwindcss').Config} */
export const content = ["./templates/**/*.html", "./static/**/*.js"];
export const theme = {
    extend: {
        colors: {
            base: {
                DEFAULT: "#1C1C1E", // background utama
                secondary: "#2A2A2E", // background sekunder / card
                text: "#F5F5F7", // teks utama
                subtext: "#C5C6C7", // teks sekunder
            },
            accent: {
                DEFAULT: "#F67280", // tombol utama / CTA
                hover: "#FFB6B9", // hover tombol
                secondary: "#6C5B7B", // aksen opsional
                link: "#FFB86C", // warna link
            },
        },
        fontFamily: {
            heading: ["Poppins", "sans-serif"],
            body: ["Inter", "sans-serif"],
        },
        borderRadius: {
            soft: "12px",
        },
    },
};
export const plugins = [];
