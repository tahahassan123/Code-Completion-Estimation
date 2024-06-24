module.exports = {
    purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                'metallic-light': '#d3d3d3',
                'metallic-dark': '#080303',
                'metallic-gradient': 'linear-gradient(45deg, #100303, #a9a9a9)',
                'metallic-shiny': 'linear-gradient(45deg, #f0f0f0, #dcdcdc)'
            },
            boxShadow: {
                'metallic': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}