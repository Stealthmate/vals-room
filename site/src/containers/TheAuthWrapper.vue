<template>
  <div>
    <v-app-bar
      app
      absolute
      color="primary"
      dark
      >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>ヴァレリの部屋</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary>
      <v-list
        nav
        dense
      >
        <v-list-item>
          <v-list-item-title><router-link :to="{name: 'TheHomePage' }">カクテル</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item v-if="user && user.is_staff">
          <v-list-item-title><router-link :to="{name: 'TheOrdersPage' }">Orders</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item v-if="user && user.is_staff">
          <v-list-item-title><router-link :to="{name: 'TheUserInvitationsPage' }">Invitations</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><v-btn @click="logout">ログアウト</v-btn></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <div>
        <router-view v-if="isLoggedIn" :user="user" />
      </div>
    </v-main>
  </div>
</template>

<script>
import {COCKTAILS, TAGS} from '@/common/data.js';

import API from '@/common/api.js';
import {isAuthenticated} from '@/common/utils.js';

export default {
  name: 'TheAuthWrapper',
  data() {
    return {
      user: null,
      tags: [],
      drawer: false
    }
  },
  computed: {
    isLoggedIn() {
      return this.user != null;
    }
  },
  created() {
    this.getMe();
  },
  beforeUpdate() {
    if(!isAuthenticated()) this.$router.push({ name: 'TheAuthPage' });
  },
  methods: {
    getMe() {
      API.auth.getMe().then(response => {
        this.user = response.data;
      }).catch(err => {
        console.log(err);
        this.$router.push({ name: 'TheAuthPage' });
      });
    },
    logout() {
      window.localStorage.removeItem('token');
      this.$router.push({ name: 'TheLoginPage' });
    }
  }
}
</script>

<style lang="scss" scoped>
.selected {
  background-color: red;
}
</style>
