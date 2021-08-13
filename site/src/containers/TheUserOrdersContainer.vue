<template>
  <v-container>
    <v-data-table
      :items="orders"
      :headers="headers"
      hide-default-header
      hide-default-footer 
      mobile-breakpoint="0"
    >
      <template #[`item.stars`]="{ item }">
        <div class="star-holder">
          <v-icon v-for="i in item.stars" :key="i">
            mdi-star
          </v-icon>
        </div>
      </template>
      <template #footer>
        <div class="total">
          Total: {{ total }}<v-icon>mdi-star</v-icon>
        </div>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import API from '@/common/api.js';

export default {
  name: 'TheCoktailsPage',
  props: {
    orders: { type: Array }
  },
  computed: {
    headers() {
      return [
        { text: 'Name', value: 'name' },
        { text: 'Stars', value: 'stars', align: 'end' },
      ];
    },
    total() {
      return this.orders.reduce((a, v) => a + v.stars, 0);
    }
  },
}
</script>

<style lang="scss" scoped>
.star-holder {
  width: 45px;
  line-height: 0;
  float: right;

  .mdi-star {
    vertical-align: middle;
    font-size: 13px;
    color: goldenrod;
  }
}

.total {
  float: right;
  font-size: 16px;

  .mdi-star {
    color: goldenrod;
    vertical-align: baseline;
    font-size: 16px;
  }
}
</style>
