<template>
  <v-container>
    <router-link :to="{name: 'TheAuthPage'}">Back</router-link>
    <v-form>
      <v-text-field v-model="username" label="Username" />
      <v-text-field v-model="password" label="Password" type="password" @keyup.enter="login" />
      <v-btn @click="login">Login</v-btn>
    </v-form>
    <SnackbarAlert ref="snackbar" />
  </v-container>
</template>

<script>
import API from '@/common/api.js';

export default {
  components: {},
  name: 'TheLoginPage',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  computed: {
    theLoginPage() { return { name: 'TheLoginPage' }; },
    theRegisterPage() { return { name: 'TheRegisterPage' }; }
  },
  methods: {
    login() {
      if(this.username.length === 0 || this.password.length === 0) {
        this.$refs.snackbar.error('Please input username and password');
        return;
      }
      API.auth.login(this.username, this.password).then(response => {
        window.localStorage.setItem('token', response.data.access);
        this.$router.push({ name: 'TheHomePage' })
      }).catch(_ => {
        this.$refs.snackbar.error('Error!');
      });
    },
    showMsg(msg) {
      this.snackbarMsg = msg;
      this.snackbar = true;
    }
  }
}
</script>