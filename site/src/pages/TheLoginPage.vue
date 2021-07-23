<template>
  <v-container>
    <v-form>
      <v-text-field v-model="username" label="Username" />
      <v-text-field v-model="password" label="Password" type="password" />
      <v-btn @click="login">Login</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import API from '@/common/api.js';

export default {
  name: 'TheLoginPage',
  data() {
    return {
      username: 'valadmin',
      password: 'valthecocktailmaster'
    }
  },
  methods: {
    login() {
      API.auth.login(this.username, this.password).then(response => {
        window.localStorage.setItem('token', response.data.access);
        this.$router.push({ name: 'TheCocktailsPage' })
      }).catch(_ => {
        alert('Error!');
      });
    }
  }
}
</script>