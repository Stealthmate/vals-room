<template>
  <v-container>
    <v-card v-for="(item, i) in theDrinks" :key="i" class="my-5">
      <v-img
        :src="getImg(item)"
        contain
        width="100vw"
      ></v-img>
      <div class="d-flex flex-grow-1 align-stretch flex-column">
        <v-card-title>{{ item.name }}</v-card-title>
        <v-card-subtitle class="d-flex flex-row">
          {{ item.reading }} <v-spacer /> {{ item.abv }}%</v-card-subtitle
        >
        <v-card-text class="text--primary">{{ item.description }}</v-card-text>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import {COCKTAILS} from '../common/data.js';

export default {
  name: 'TheCoktailsPage',
  computed: {
    theDrinks() {
      return COCKTAILS;
    }
  },
  methods: {
    getImg(item) {
      return `${process.env.BASE_URL}assets/${item.img}`;
    }
  }
}
</script>

<style scoped>
ruby:nth-child(n + 2)::before {
  content: "\00a0";
}
</style>
