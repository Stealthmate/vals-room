<template>
  <v-container class="d-flex flex-column align-center">
    <v-btn class="ma-5 blue lighten-3" :to="theLoginPage">Login</v-btn>
    <v-btn class="ma-5" :to="theRegisterPage"> Register </v-btn>
  </v-container>
</template>

<script>

export default {
  name: 'TheAuthPage',
  computed: {
    theLoginPage() { return { name: 'TheLoginPage' }; },
    theRegisterPage() { return { name: 'TheRegisterPage' }; }
  },
  // created() {
  //   if(this.$router.currentRoute.name !== 'TheHomePage') this.$router.push({ name: 'TheHomePage'});
  // },
}
</script>