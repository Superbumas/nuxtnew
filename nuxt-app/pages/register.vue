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
            <p v-if="emailError" class="text-red-500 text-sm">{{ emailError }}</p>
          </div>
          <div class="mb-4">
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input v-model="password" type="password" id="password" required
                   class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-500" />
            <p v-if="passwordError" class="text-red-500 text-sm">{{ passwordError }}</p>
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
          const response = await fetch('http://172.104.224.207:5000/api/csrf-token');
          const data = await response.json();
          this.csrfToken = data.csrf_token;  // Store the CSRF token
        } catch (error) {
          console.error('Error fetching CSRF token:', error);
        }
      },
      validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;  // Simple email regex
        return re.test(String(email).toLowerCase());
      },
      validatePassword(password) {
        // Password must be at least 8 characters long and contain at least one number and one special character
        const re = /^(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
        return re.test(password);
      },
      async registerUser() {
        // Reset errors
        this.emailError = '';
        this.passwordError = '';
  
        // Validate email
        if (!this.validateEmail(this.email)) {
          this.emailError = 'Invalid email format.';
          return;
        }
  
        // Validate password
        if (!this.validatePassword(this.password)) {
          this.passwordError = 'Password must be at least 8 characters long and contain at least one number and one special character.';
          return;
        }
  
        try {
          const response = await this.$axios.$post('http://172.104.224.207:5000/api/register', {
            username: this.username,
            email: this.email,
            password: this.password,
            confirm_password: this.confirmPassword,
            csrf_token: this.csrfToken  // Include CSRF token
          }, {
            headers: {
              'Content-Type': 'application/json'  // Set content type to JSON
            }
          });
          console.log('Registration successful:', response);
          // Optionally, redirect or show a success message here
        } catch (error) {
          // Enhanced error handling
          if (error.response) {
            console.error('Registration failed:', error.response.data);
            alert(`Error: ${error.response.data.error || 'Registration failed'}`);
          } else {
            console.error('Registration failed:', error);
            alert('An unexpected error occurred.');
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles here if needed */
  </style>