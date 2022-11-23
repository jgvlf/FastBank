/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      
      'mobileS': '281px',
      // => @media (min-width: 280px) { ... }

      'mobileM': '375px',
      // => @media (min-width: 393px) { ... }

      'mobileL': '412px',
      // => @media (min-width: 412px) { ... }
      
      'tablet': '640px',
      // => @media (min-width: 640px) { ... }

      
      'default': '1280px',
      // => @media (min-width: 1280px) { ... }

    },
    extend: {
      backgroundImage: {
        'fast-effect': "url('./src/assets/img/fast_effect_001.png')",
        'thunder-effect': "url('./src/assets/img/thunder_effect_001.png')",
      },
    },
  },
  plugins: [],
}
