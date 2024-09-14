<template>
    <div>
      <h1>Welcome to Memorial App</h1>
      <p v-if="user">Hello, {{ user.username }}</p>
      <p v-else>Please log in to manage your memorial profiles.</p>
    </div>
  </template>

  <script>
  export default {
    computed: {
      user() {
        return this.$auth.user
      }
    }
  }
  </script>