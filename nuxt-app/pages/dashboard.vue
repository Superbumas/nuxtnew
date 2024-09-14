<template>
  <div class="dashboard-container">
    <div class="header">
      <h2 class="text-2xl font-bold mb-6">Your Profiles</h2>
      <button @click="createProfile" class="create-profile-button">Create Profile</button>
    </div>
    <table class="profile-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Created At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="profile in profiles" :key="profile.id">
          <td><a :href="'/profile/' + profile.id">{{ profile.name }}</a></td>
          <td>{{ profile.created_at }}</td>
          <td>
            <a :href="'/profile/' + profile.id">View</a> |
            <a :href="'/profile/edit/' + profile.id">Edit</a> |
            <a href="#" @click.prevent="deleteProfile(profile.id)" class="delete-link">Delete</a>
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="logout" class="logout-button">Logout</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      profiles: []  // Fetch profiles from your API
    }
  },
  methods: {
    async createProfile() {
      // Logic to create a profile
    },
    async deleteProfile(id) {
      // Logic to delete a profile
    },
    async logout() {
      try {
        await this.$auth.logout()
        this.$router.push('/login')
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted() {
    // Fetch profiles when the component is mounted
    try {
      const response = await this.$axios.get('/api/profiles')
      this.profiles = response.data
    } catch (error) {
      console.error(error)
    }
  }
}
</script>

<style scoped>
@import '~/assets/form-styles.css'; /* Import common styles */

.dashboard-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.create-profile-button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.create-profile-button:hover {
  background-color: #0056b3;
}

.profile-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.profile-table th, .profile-table td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: left;
}

.profile-table th {
  background-color: #f1f1f1;
}

.delete-link {
  color: red;
  cursor: pointer;
}

.logout-button {
  background-color: #dc3545;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #c82333;
}
</style>