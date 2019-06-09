import pkg from './package'
const webpack = require('webpack')

export default {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Abiella and Brian are Getting Married!',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' },
      // {
      //   rel: 'stylesheet',
      //   href: 'https://api.tiles.mapbox.com/mapbox-gl-js/v0.51.0/mapbox-gl.css'
      // },
    ]
  },
  render: {
    static: {
      maxAge: 1000 * 60 * 60 * 24 * 7
    }
  },

  /*
  ** Customize the progress-bar color
  */
 loading: {
  color: '#8CA0D7'
},

  /*
  ** Global CSS
  */
  css: [
    // Load a Node.js module directly (here it's a Sass file)
    // 'bulma',
    // SCSS file in the project
    '@/assets/css/main.scss',
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // 'nuxt-sass-resources-loader', 
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    // Doc:https://github.com/nuxt-community/modules/tree/master/packages/bulma
    // '@nuxtjs/bulma',
    ['@nuxtjs/google-analytics', {
      id: 'UA-141695537-1'
    }]
  ],
  // sassResources: [
  //   '@/assets/css/main.scss',
  // ],
  /*
  ** Axios module configuration
  */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
  },

  /*
  ** Build configuration
  */
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false
        }
      }
    },
    plugins: [
      new webpack.ProvidePlugin({
        mapboxgl: 'mapbox-gl'
      })
    ],
    /*
    ** You can extend webpack config here
    */
    // extend(config, ctx) {
    //   // Run ESLint on save
    //   if (ctx.isDev && ctx.isClient) {
    //     config.module.rules.push({
    //       enforce: 'pre',
    //       test: /\.(js|vue)$/,
    //       loader: 'eslint-loader',
    //       exclude: /(node_modules)/
    //     })
    //   }
    // }
  },
  server: {
    port: 8080, // default: 3000
    host: 'localhost', // default: localhost
  },
}
