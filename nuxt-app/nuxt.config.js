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
      baseURL: 'http://localhost:5000' // Adjust the port if your Flask server is running on a different port
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
            login: { url: '/api/login', method: 'post' },
            logout: { url: '/api/logout', method: 'post' },
            user: { url: '/api/user', method: 'get' }
          }
        }
      }
    },
    build: {},
    server: {
      port: 3000, // default: 3000
      host: 'localhost' // default: localhost
    }
  }