<template>
  <div class="form-container">
    <h1 class="text-2xl font-bold mb-6 text-center">Welcome to the Memorial App</h1>
    <div v-if="$auth.loggedIn">
      <p class="text-center">Hello, {{ $auth.user.first_name }}!</p>
      <button @click="logout" class="form-button">Logout</button>
    </div>
    <div v-else>
      <nuxt-link to="/login" class="form-button">Login</nuxt-link> | 
      <nuxt-link to="/register" class="form-button">Register</nuxt-link>
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

<style scoped>
@import '~/assets/form-styles.css'; /* Import common styles */
</style>