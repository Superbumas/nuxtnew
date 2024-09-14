<template>
    <div class="profile-form">
      <h2>Profile</h2>
      <p>This information will be displayed publicly so be careful what you share.</p>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="first_name">First name</label>
          <input type="text" v-model="form.first_name" id="first_name" required />
        </div>
        <div class="form-group">
          <label for="last_name">Last name</label>
          <input type="text" v-model="form.last_name" id="last_name" required />
        </div>
        <div class="form-group">
          <label for="biography">Bio</label>
          <textarea v-model="form.biography" id="biography" required></textarea>
          <small>Write a few sentences about yourself.</small>
        </div>
        <div class="form-group">
          <label for="profile_photo_url">Profile Picture</label>
          <input type="file" @change="handleFileUpload('profile_photo_url', $event)" id="profile_photo_url" />
        </div>
        <div class="form-group">
          <label for="cover_photo_url">Cover Photo</label>
          <input type="file" @change="handleFileUpload('cover_photo_url', $event)" id="cover_photo_url" />
        </div>
        <div class="form-group">
          <label for="date_of_birth">Date of Birth</label>
          <input type="date" v-model="form.date_of_birth" id="date_of_birth" required />
        </div>
        <div class="form-group">
          <label for="date_of_death">Date of Death</label>
          <input type="date" v-model="form.date_of_death" id="date_of_death" required />
        </div>
        <div class="form-group">
          <label for="country">Country</label>
          <input type="text" v-model="form.country" id="country" required />
        </div>
        <div class="form-group">
          <label for="city">City</label>
          <input type="text" v-model="form.city" id="city" required />
        </div>
        <div class="form-group">
          <label for="timeline_events">Timeline Events</label>
          <textarea v-model="form.timeline_events" id="timeline_events"></textarea>
          <a href="#" @click.prevent="addEvent">Add Event</a>
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
        <button type="button" class="btn btn-secondary" @click="cancel">Cancel</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          first_name: '',
          last_name: '',
          biography: '',
          profile_photo_url: '',
          cover_photo_url: '',
          date_of_birth: '',
          date_of_death: '',
          country: '',
          city: '',
          timeline_events: ''
        },
        csrfToken: ''
      };
    },
    async created() {
      await this.fetchCsrfToken();
    },
    methods: {
      async fetchCsrfToken() {
        try {
          const response = await fetch('http://172.104.224.207:5000/api/csrf-token');
          const data = await response.json();
          this.csrfToken = data.csrf_token;
        } catch (error) {
          console.error('Error fetching CSRF token:', error);
        }
      },
      handleFileUpload(field, event) {
        const file = event.target.files[0];
        this.form[field] = file;
      },
      async submitForm() {
        const formData = new FormData();
        for (const key in this.form) {
          formData.append(key, this.form[key]);
        }
        formData.append('csrf_token', this.csrfToken);  // Include CSRF token
  
        try {
          const response = await fetch('http://172.104.224.207:5000/api/memorials', {
            method: 'POST',
            body: formData
          });
          if (response.ok) {
            // Handle successful form submission
            console.log('Form submitted successfully');
          } else {
            // Handle form submission error
            console.error('Form submission error:', response.statusText);
          }
        } catch (error) {
          console.error('Error submitting form:', error);
        }
      },
      addEvent() {
        // Logic to add a new event
      },
      cancel() {
        // Logic to handle form cancellation
      }
    }
  };
  </script>
  
  <style scoped>
  .profile-form {
    max-width: 600px;
    margin: 0 auto;
  }
  .form-group {
    margin-bottom: 1rem;
  }
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
  }
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .form-group small {
    display: block;
    margin-top: 0.5rem;
    color: #666;
  }
  .btn {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .btn-primary {
    background-color: #007bff;
    color: #fff;
  }
  .btn-secondary {
    background-color: #6c757d;
    color: #fff;
  }
  </style>