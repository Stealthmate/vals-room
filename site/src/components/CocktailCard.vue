<template>
  <v-card
    class="my-5" 
    max-width="500px">
      <div class="d-flex flex-grow-1 align-stretch flex-column">
        <v-card-title>
          {{ cocktail.name }}
          <v-spacer />
          <div class="star-holder">
            <v-icon v-for="i in cocktail.stars" :key="i">
              mdi-star
            </v-icon>
          </div>
        </v-card-title>
        <v-card-subtitle class="d-flex flex-row">
          {{ cocktail.reading }}
          <v-spacer />
          {{ Math.round(cocktail.abv) }} %
        </v-card-subtitle>
        <v-card-text class="text--primary">{{ cocktail.description }}</v-card-text>
        <div class="px-4 pb-4">
          <v-chip v-for="(t, i) in cocktail.tags" :key="i" small class="mx-1">{{t.name}}</v-chip>
        </div>
      </div>
      <v-card-actions class="justify-end">
        <v-btn @click="$emit('order')">Order</v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
export default {
  name: 'CocktailCard',
  props: {
    cocktail: { type: Object }
  },
  data() {
    return {
      inDialog: false,
    }
  },
  methods: {
    getImg() {
      return `${process.env.BASE_URL}assets/${this.cocktail.img}`;
    }
  }
}
</script>

<style lang="scss" scoped>
.star-holder {
  text-align: end;
  width: 45px;
  line-height: 0;

  .mdi-star {
    vertical-align: middle;
    font-size: 13px;
    color: goldenrod;
  }
}
</style>
