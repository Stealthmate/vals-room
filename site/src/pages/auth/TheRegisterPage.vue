<template>
  <v-container>
    <router-link :to="{name: 'TheAuthPage'}">Back</router-link>
    <v-form v-model="valid" ref="form" lazy-validation class="d-flex flex-column">
      <v-text-field v-model="invitation" label="Invitation Number" required :rules="rules" autocomplete="off" />
      <v-text-field v-model="username" label="Username" required :rules="rules" autocomplete="off" />
      <v-text-field v-model="password" label="Password" type="password" required :rules="rules" autocomplete="off" />
      <v-text-field v-model="name" label="Name" required :rules="rules" autocomplete="off" />
      <v-btn class="align-self-center ma-5" @click="register">Register</v-btn>
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
      valid: false,
      invitation: '',
      username: '',
      password: '',
      name: '',
    }
  },
  computed: {
    rules() { return [ v => !!v || 'Field is required.' ]}
  },
  methods: {
    register() {
      let isValid = this.$refs.form.validate();
      if(!isValid) return;
      API.auth.register(this.invitation, this.username, this.password, this.name).then(response => {
        this.$refs.snackbar.success('OK!');
        let router = this.$router;
        setTimeout(() => router.push({ name: 'ThePublicHomePage' }), 500);
      }).catch(_ => {
        this.$refs.snackbar.error('Error!');
      });
    },
  }
}
</script>