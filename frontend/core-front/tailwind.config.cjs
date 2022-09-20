/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      
      'mobileS': '280px',
      // => @media (min-width: 280px) { ... }

      'mobileM': '375px',
      // => @media (min-width: 393px) { ... }

      'mobileL': '412px',
      // => @media (min-width: 412px) { ... }
      
      'tablet': '640px',
      // => @media (min-width: 640px) { ... }

      'tablet': '640px',
      // => @media (min-width: 640px) { ... }
      
      'default': '1280px',
      // => @media (min-width: 1920px) { ... }

    },
    extend: {},
  },
  plugins: [],
}
