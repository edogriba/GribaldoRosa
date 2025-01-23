module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary : {
          50: '#f2e6ff',
          100: '#d9b3ff',
          200: '#bf80ff',
          300: '#a64dff',
          400: '#8c1aff',
          500: '#7300e6',
          600: '#5900b3',
          700: '#400080',
          800: '#26004d',
          900: '#130026',
        },
        secondary: {
          50: '#f5f7ff',
          100: '#ebefff',
          200: '#d6dfff',
          300: '#c2cfff',
          400: '#adbfff',
          500: '#99afff',
          600: '#7a8fcc',
          700: '#5c6f99',
          800: '#3d4f66',
          900: '#1f2833',
    },
    },
  },
},
  plugins: [
    require('flowbite/plugin')
  ],
};
