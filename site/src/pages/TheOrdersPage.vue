<template>
  <v-card flat>
    <v-tabs v-model="tab">
      <v-tab>Active Orders</v-tab>
      <v-tab>Bills</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item :key="1" :value="0">
        <TheActiveOrdersContainer />
      </v-tab-item>
      <v-tab-item :key="2" :value="1">
        <TheBillContainer />
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>

import API from '@/common/api.js';

import TheActiveOrdersContainer from "@/containers/TheActiveOrdersContainer";
import TheBillContainer from "@/containers/TheBillContainer";

const hasTagId = (xs, tid) => xs.some((x) => x.id === tid);

export default {
  name: "TheCoktailsPage",
  components: { TheActiveOrdersContainer, TheBillContainer },
  data() {
    return {
      tab: 0
    }
  }
};
</script>
