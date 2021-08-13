<template>
  <v-card flat>
    <v-tabs v-model="tab">
      <v-tab>Cocktails</v-tab>
      <v-tab>Orders</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item :key="1" :value="0">
        <TheCocktailsContainer :drinks="drinks" @order="refresh"/>
      </v-tab-item>
      <v-tab-item :key="2" :value="1">
        <TheUserOrdersContainer :orders="orders" />
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>

import API from '@/common/api.js';

import TheCocktailsContainer from "@/containers/TheCocktailsContainer";
import TheUserOrdersContainer from "@/containers/TheUserOrdersContainer";

const hasTagId = (xs, tid) => xs.some((x) => x.id === tid);

export default {
  name: "TheCoktailsPage",
  components: { TheCocktailsContainer, TheUserOrdersContainer },
  data() {
    return {
      drinks: [],
      orders: [],
      tab: 0
    }
  },
  created() {
    this.refresh();
  },
  methods: {
    refresh() {
      API.drinks.getAll().then(response => {
        this.drinks = response.data;
      });
      API.orders.listUserOrders().then(response => {
        this.orders = response.data;
      })
    }
  }
};
</script>
