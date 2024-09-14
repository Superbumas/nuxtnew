<template>
  <div>
    <h1>User Dashboard</h1>
    <form @submit.prevent="createProfile">
      <div>
        <label for="name">Name:</label>
        <input type="text" v-model="profile.name" id="name" required />
      </div>
      <div>
        <label for="birthdate">Birthdate:</label>
        <input type="date" v-model="profile.birthdate" id="birthdate" required />
      </div>
      <div>
        <label for="deathdate">Deathdate:</label>
        <input type="date" v-model="profile.deathdate" id="deathdate" required />
      </div>
      <div>
        <label for="biography">Biography:</label>
        <textarea v-model="profile.biography" id="biography" required></textarea>
      </div>
      <button type="submit">Create Profile</button>
    </form>

    <div v-if="profiles.length">
      <h2>Existing Profiles</h2>
      <ul>
        <li v-for="profile in profiles" :key="profile.id">
          {{ profile.name }} ({{ profile.birthdate }} - {{ profile.deathdate }})
          <button @click="deleteProfile(profile.id)">Delete</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      profile: {
        name: '',
        birthdate: '',
        deathdate: '',
        biography: ''
      },
      profiles: []
    };
  },
  methods: {
    async createProfile() {
      try {
        const response = await axios.post('http://localhost:5000/api/memorials', this.profile);
        this.profiles.push(response.data);
        this.resetForm();
      } catch (error) {
        console.error('Error creating profile:', error);
      }
    },
    async fetchProfiles() {
      try {
        const response = await axios.get('http://localhost:5000/api/memorials');
        this.profiles = response.data;
      } catch (error) {
        console.error('Error fetching profiles:', error);
      }
    },
    async deleteProfile(id) {
      try {
        await axios.delete(`http://localhost:5000/api/memorials/${id}`);
        this.profiles = this.profiles.filter(profile => profile.id !== id);
      } catch (error) {
        console.error('Error deleting profile:', error);
      }
    },
    resetForm() {
      this.profile = {
        name: '',
        birthdate: '',
        deathdate: '',
        biography: ''
      };
    }
  },
  mounted() {
    this.fetchProfiles();
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>