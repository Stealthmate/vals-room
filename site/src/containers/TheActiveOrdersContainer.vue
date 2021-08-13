<template>
  <v-container>
    <v-list>
      <OrderCard v-for="(o, i) in orders" :order="o" :key="i" @complete="complete(o)" @cancel="cancel(o)"/>
    </v-list>
    <SnackbarAlert ref="snackbar" />
  </v-container>
</template>

<script>
import API from '@/common/api.js';
import OrderCard from '@/components/OrderCard';

export default {
  name: 'TheActiveOrdersContainer',
  components: {
    OrderCard
  },
  data() {
    return {
      orders: []
    }
  },
  created() {
    this.fetch();
  },
  methods: {
    fetch() {
      API.orders.listActiveOrders().then(response => {
        this.orders = response.data;
      }).catch(err => {
        this.$refs.snackbar.error('API Error!');
        console.log(err);
      });
    },
    complete(o) {
      API.orders.complete(o.id).then(response => {
        this.$refs.snackbar.success('Order completed');
        this.fetch();
      }).catch(err => {
        this.$refs.snackbar.error('API Error!');
      });
    },
    cancel(o) {
      API.orders.cancel(o.id).then(response => {
        this.$refs.snackbar.success('Order cancelled');
        this.fetch();
      }).catch(err => {
        this.$refs.snackbar.error('API Error!');
      })
    }
  }
}
</script>