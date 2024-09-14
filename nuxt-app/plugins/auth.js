export default function ({ $auth }) {
    if (!$auth) {
      console.error('Auth module is not initialized')
      return
    }

    $auth.onRedirect((to, from) => {
      console.log('Redirecting from', from, 'to', to)
      // you can optionally change `to` by returning a new value
      return to
    })
  }