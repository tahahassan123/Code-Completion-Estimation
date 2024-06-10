module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        metallic: {
          light: '#b0bec5',
          DEFAULT: '#607d8b',
          dark: '#37474f',
          shiny: '#e0e0e0',
        },
      },
      backgroundImage: theme => ({
        'metallic-gradient': 'linear-gradient(to right, #37474f, #b0bec5)',
      }),
      boxShadow: {
        'metallic': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      },
    },
  },
  plugins: [],
};
