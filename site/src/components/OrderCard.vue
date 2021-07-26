<template>
  <v-card class="ma-5">
    <v-card-title> {{ order.recipe.name }} </v-card-title>
    <v-card-subtitle> {{ order.name }} </v-card-subtitle>
    <v-card-text>
      <v-data-table
        :headers="headers"
        :items="order.recipe.ingredients"
        dense
        hide-default-footer
        mobile-breakpoint="0"
        sort-by="amount"
        sort-desc
      />
    </v-card-text>
  <v-card-actions class="justify-space-between">
    <v-btn @click="$emit('cancel')">Cancel</v-btn>
    <v-btn @click="$emit('complete')" class="blue lighten-3">Complete</v-btn>
  </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'OrderCard',
  props: {
    order: { type: Object }
  },
  computed: {
    headers() {
      return [
        { text: 'Name', value: 'name' },
        { text: 'Amount', value: 'amount' }
      ]
    }
  }
}
</script>