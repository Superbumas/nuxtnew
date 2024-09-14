<template>
  <div class="form-container">
    <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email</label>
        <input type="email" v-model="form.email" class="form-input" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" v-model="form.password" class="form-input" required />
      </div>
      <button type="submit" class="form-button">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith('local', { data: this.form })
        this.$router.push('/dashboard')
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