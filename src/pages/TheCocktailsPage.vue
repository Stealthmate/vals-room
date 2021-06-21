<template>
  <v-container>
    <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header>
        絞り込み
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-chip
          v-for="(t, i) in theTags"
          :key="i"
          class="ma-1"
          :color="t.color"
          @click="() => toggleTag(t.name)"
        >{{t.name}}</v-chip>
      </v-expansion-panel-content>
    </v-expansion-panel>
    </v-expansion-panels>
    <CocktailCard v-for="(drink, i) in theDrinks" :key="i" :cocktail="drink" />
  </v-container>
</template>

<script>
import {COCKTAILS, TAGS} from '../common/data.js';
import CocktailCard from '@/components/CocktailCard';

export default {
  name: 'TheCoktailsPage',
  components: { CocktailCard },
  data() {
    return {
      tags: []
    }
  },
  computed: {
    theDrinks() {
      return COCKTAILS.filter(cocktail => {
        if(this.tags.length == 0) return true;
        return this.tags.every(t => cocktail.tags.includes(t));
      });
    },
    theTags() {
      return TAGS.map(t => ({
        name: t,
        selected: this.tags.includes(t),
        color: this.tags.includes(t) ? 'blue' : ''
      }));
    }
  },
  methods: {
    getImg(item) {
      return `${process.env.BASE_URL}assets/${item.img}`;
    },
    toggleTag(t) {
      if(this.tags.includes(t)) this.tags.splice(this.tags.indexOf(t), 1);
      else this.tags.push(t);
    },
    tagClass(t) {
      if(this.tags.includes(t)) return 'selected';
      return '';
    }
  }
}
</script>

<style lang="scss" scoped>
.selected {
  background-color: red;
}
</style>
