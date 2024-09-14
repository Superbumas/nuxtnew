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
        confirmPassword: '',
        csrfToken: '',  // Store CSRF token
        emailError: '',
        passwordError: ''
      };
    },
    async created() {
      await this.fetchCsrfToken();  // Fetch CSRF token on component creation
    },
    methods: {
      async fetchCsrfToken() {
        try {
          const response = await fetch('/api/csrf-token');
          const data = await response.json();
          this.csrfToken = data.csrf_token;  // Store the CSRF token
        } catch (error) {
          console.error('Error fetching CSRF token:', error);
        }
      },
      async registerUser() {
        try {
          const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'csrf-token': this.csrfToken, // Include CSRF token in headers
            },
            body: JSON.stringify({
              username: this.username,
              email: this.email,
              password: this.password,
              confirm_password: this.confirmPassword,
              csrf_token: this.csrfToken,  // Include CSRF token in body
            }),
          });
  
          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Registration failed');
          }
  
          const result = await response.json();
          console.log('Registration successful:', result);
          // Optionally, redirect or show a success message here
        } catch (error) {
          console.error('Registration failed:', error);
          alert(`Error: ${error.message}`);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles here if needed */
  </style>