<template>
  <v-snackbar v-model="snackbar" :timeout="timeout" :color="`${color} lighten-3`">
    {{ snackbarMsg }}
  </v-snackbar>
</template>

<script>
export default {
  name: 'SnackbarAlert',
  props: {
    timeout: { type: Number, default: 2000 }
  },
  data() {
    return {
      snackbar: false,
      snackbarMsg: '',
      color: 'green'
    }
  },
  computed: {
    colorError() { return 'red lighten-2'; },
    colorSuccess() { return 'green lighten-2'; }
  },
  methods: {
    showMsg(msg) {
      this.snackbarMsg = msg;
      this.snackbar = true;
    },
    success(msg) {
      this.color = this.colorSuccess;
      this.showMsg(msg);
    },
    error(msg) {
      this.color = this.colorError;
      this.showMsg(msg);
    }
  }
}
</script>