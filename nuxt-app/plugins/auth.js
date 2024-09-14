export default function ({ $auth }) {
  console.log('Auth plugin loaded')
  if (!$auth.loggedIn) {
    return
  }

  const username = $auth.user.username
  console.log(`Logged in as: ${username}`)
}