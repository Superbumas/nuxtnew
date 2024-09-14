// nuxt.config.js
export default defineNuxtConfig({
  ssr: true,
  target: 'server',
  head: {
    title: 'Memorial App',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  css: [],
  plugins: [
    '~/plugins/axios.js',
    '~/plugins/auth.js'
  ],
  components: true,
  buildModules: [
    '@nuxt/postcss8',
    '@nuxtjs/tailwindcss'
  ],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/dotenv',
    'nuxt-csurf'  // Add the CSRF module here
  ],
  axios: {
    baseURL: 'http://172.104.224.207:5000/api' // Flask API
  },
  auth: {
    strategies: {
      local: {
        token: {
          property: 'token',
          global: true,
          required: true,
          type: 'Bearer'
        },
        user: {
          property: 'user',
          autoFetch: true
        },
        endpoints: {
          login: { url: '/login', method: 'post' },
          logout: { url: '/logout', method: 'post' },
          user: { url: '/user', method: 'get' }
        }
      }
    },
    plugins: ['~/plugins/auth.js']
  },
  build: {},
  server: {
    port: 3000,
    host: '0.0.0.0'
  },
  csurf: {
    https: false, // Set to true in production
    cookieKey: '', // Specify your cookie key here
    methodsToProtect: ['POST', 'PUT', 'PATCH'], // Specify methods to protect
    headerName: 'csrf-token' // Specify the header name for CSRF token
  }
});