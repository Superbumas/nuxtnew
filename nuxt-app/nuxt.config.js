export default {
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
  buildModules: [],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/dotenv'
  ],
  axios: {
    baseURL: 'http://localhost:5000/api' // Ensure the base URL matches your Flask API
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
    plugins: ['~/plugins/auth.js'] // Ensure the auth plugin is included
  },
  build: {},
  server: {
    port: 3000, // default: 3000
    host: '0.0.0.0' // default: localhost
  }
}