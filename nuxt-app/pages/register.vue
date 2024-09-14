<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="email">Email</label>
          <input type="email" v-model="form.email" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" v-model="form.password" required />
        </div>
        <div>
          <label for="first_name">First Name</label>
          <input type="text" v-model="form.first_name" required />
        </div>
        <div>
          <label for="last_name">Last Name</label>
          <input type="text" v-model="form.last_name" required />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          email: '',
          password: '',
          first_name: '',
          last_name: ''
        }
      }
    },
    methods: {
      async register() {
        try {
          await this.$axios.post('/register', this.form)
          this.$router.push('/login')
        } catch (error) {
          console.error(error)
        }
      }
    }
  }
  </script>