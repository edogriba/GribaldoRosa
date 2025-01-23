module.exports = {
  content: [
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#7859aa',
          DEFAULT: '#34047c',
          dark: '#34047c',
        },
        secondary: {
          light: '#d3c9e3',
          DEFAULT: '#34047c',
          dark: '#9c7cbc',
        }
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
};
