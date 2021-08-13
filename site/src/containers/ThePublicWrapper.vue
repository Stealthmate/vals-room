<template>
  <div>
    <router-view />
  </div>
</template>

<script>

import { isAuthenticated } from '@/common/utils.js';

export default {
  name: 'ThePublicWrapper',
  created() {
    this.refresh();
  },
  methods: {
    refresh() {
      if(isAuthenticated()) this.$router.push({ name: 'TheHomePage' });
    }
  }
}
</script>