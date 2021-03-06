import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';

import AppPage from '@/components/AppPage';
import SnackbarAlert from '@/components/SnackbarAlert';

import router from '@/pages/router.js';

Vue.config.productionTip = false

Vue.component('AppPage', AppPage);
Vue.component('SnackbarAlert', SnackbarAlert);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
