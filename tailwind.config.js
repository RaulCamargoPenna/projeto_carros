module.exports = {
  content: [
      'app/templates/**/*.html',
      'cars/templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      '.static/src/**/*.{html,js}'
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
  
}

// No content eu precciso colocar todos os caminhos que possuem os templates, se não ele não vai aplicar formatações dos frameworks neles.