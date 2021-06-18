<template>
  <v-container>
    <CocktailCard v-for="(drink, i) in theDrinks" :key="i" :cocktail="drink" />
  </v-container>
</template>

<script>
import {COCKTAILS} from '../common/data.js';
import CocktailCard from '@/components/CocktailCard';

export default {
  name: 'TheCoktailsPage',
  components: { CocktailCard },
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
