<template>
  <v-app>
    <v-app-bar
      app
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
          <v-list-item-title><router-link :to="{name: 'TheCocktailsPage' }">カクテル</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item>
          <v-list-item-title><router-link :to="{name: 'TheBottlesPage' }">ボトル紹介</router-link></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      drawer: false
    }
  }
};
</script>
