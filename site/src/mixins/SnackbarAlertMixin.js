export default {
  name: 'SnackbarAlertMixin',
  data() {
    return {
      snackbar: false,
      snackbarMsg: undefined
    }
  },
  methods: {
    snackbarAlert(msg) {
      this.snackbar = true;
      this.snackbarMsg = msg;
    }
  }
}