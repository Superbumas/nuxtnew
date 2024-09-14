export default function ({ $auth }) {
  console.log('Auth plugin loaded')
  $auth.onError((error, name, endpoint) => {
    console.error(name, error)
  })
}