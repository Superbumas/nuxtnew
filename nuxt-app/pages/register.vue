<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="bg-white p-8 rounded-lg shadow-md w-96">
        <h2 class="text-2xl font-bold mb-6 text-center">Register</h2>
        <form @submit.prevent="registerUser">
          <div class="mb-4">
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input v-model="username" type="text" id="username" required
                   class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-500" />
          </div>
          <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input v-model="email" type="email" id="email" required
                   class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-500" />
          </div>
          <div class="mb-4">
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input v-model="password" type="password" id="password" required
                   class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-500" />
          </div>
          <div class="mb-6">
            <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirm Password</label>
            <input v-model="confirmPassword" type="password" id="confirmPassword" required
                   class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-500" />
          </div>
          <button type="submit" class="w-full bg-blue-500 text-white font-bold py-2 rounded-md hover:bg-blue-600 transition duration-200">Sign Up</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      };
    },
    methods: {
      async registerUser() {
        try {
          const response = await this.$axios.$post('/register', {
            username: this.username,
            email: this.email,
            password: this.password,
            confirm_password: this.confirmPassword
          });
          console.log('Registration successful:', response);
        } catch (error) {
          console.error('Registration failed:', error.response.data);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles here if needed */
  </style>