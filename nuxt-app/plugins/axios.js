export default function ({ $axios, redirect }) {
  console.log('Axios plugin loaded')
  $axios.onError(error => {
    if (error.response && error.response.status === 401) {
      redirect('/login')
    }
  })
}