export default function ({ $auth }) {
  console.log('Auth plugin loaded')
  if (!$auth || !$auth.loggedIn) {
    console.log('User is not logged in or $auth is not defined')
    return
  }

  const username = $auth.user.username
  console.log(`Logged in as: ${username}`)
}