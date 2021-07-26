<template>
  <v-container>
    <v-text-field label="Name" v-model="name" />
    <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header>
        絞り込み
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-chip
          v-for="(t, i) in filteredTags"
          :key="i"
          :class="`ma-1 ${tagClass(t)}`"
          :color="t.color"
          @click="() => toggleTag(t)"
        >{{t.name}}</v-chip>
      </v-expansion-panel-content>
    </v-expansion-panel>
    </v-expansion-panels>
    <CocktailCard v-for="(drink, i) in filteredDrinks" :key="i" :cocktail="drink" @order="() => order(drink)" />
    <SnackbarAlert ref="snackbar" />
  </v-container>
</template>

<script>
import CocktailCard from '@/components/CocktailCard';
import API from '@/common/api.js';

const hasTagId = (xs, tid) => xs.some(x => x.id === tid);

export default {
  name: 'TheCoktailsPage',
  components: { CocktailCard },
  data() {
    return {
      drinks: [],
      tags: [],
      selectedTags: [],
    }
  },
  computed: {
    filteredTags() {
      console.log(this.selectedTags);
      if(this.selectedTags.length === 0) return this.tags;
      return this.tags.filter(t => this.drinks.some(d => [t, ...this.selectedTags].every(t1 => hasTagId(d.tags, t1.id))));
    },
    filteredDrinks() {
      if(this.selectedTags === []) return this.drinks;
      return this.drinks.filter(d => this.selectedTags.every(t => hasTagId(d.tags, t.id)));
    },
    name: {
      get() {
        return window.localStorage.getItem('name')
      },
      set(v) {
        window.localStorage.setItem('name', v)
      }
    },
  },
  created() {
    this.fetch();
  },
  methods: {
    fetch() {
      API.getDrinks().then(response => {
        this.drinks = response.data;
      });
      API.getTags().then(response => {
        this.tags = response.data;
      });
    },
    getImg(item) {
      return `${process.env.BASE_URL}assets/${item.img}`;
    },
    toggleTag(t) {
      if(this.selectedTags.includes(t)) this.selectedTags.splice(this.selectedTags.indexOf(t), 1);
      else this.selectedTags.push(t);
    },
    tagClass(t) {
      console.log(hasTagId(this.selectedTags, t.id))
      if(hasTagId(this.selectedTags, t.id)) return 'selected';
      return '';
    },
    order(drink) {
      API.orderItem(this.name, drink.id).then(response => {
        this.$refs.snackbar.success(`Ordered a ${drink.name}!`);
      }).catch(err => {
        this.$refs.snackbar.error('Error!');
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.selected {
  color: red !important;
}
</style>
