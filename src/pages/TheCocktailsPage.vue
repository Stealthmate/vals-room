<template>
  <v-container>
    <v-card v-for="(item, i) in theDrinks" :key="i" class="my-5">
      <v-img
        :src="require(`@/assets/${item.img}`)"
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
import COCKTAILS from '@/common/cocktails.json';
const IN_STOCK = [
  'Ocean Water',
  'Blue Lagoon',
  'Tequila Sunrise',
  'Midori June Bug'
];

  export default {
    name: 'TheCoktailsPage',
    computed: {
      theDrinks() {
        return COCKTAILS.filter(x => IN_STOCK.includes(x.name));
      }
    }
  }
</script>

<style scoped>
ruby:nth-child(n + 2)::before {
  content: "\00a0";
}
</style>
