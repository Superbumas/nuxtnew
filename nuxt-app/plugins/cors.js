export default function ({ $axios }) {
    $axios.onRequest(config => {
      config.headers.common['Access-Control-Allow-Origin'] = '*'
      return config
    })
  }