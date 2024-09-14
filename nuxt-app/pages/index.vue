<template>
  <div>
    <h1>Welcome to the Memorial App</h1>
    <div v-if="$auth.loggedIn">
      <p>Hello, {{ $auth.user.first_name }}!</p>
      <button @click="logout">Logout</button>
    </div>
    <div v-else>
      <nuxt-link to="/login">Login</nuxt-link> | 
      <nuxt-link to="/register">Register</nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    async logout() {
      try {
        await this.$auth.logout()
        this.$router.push('/login')
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>