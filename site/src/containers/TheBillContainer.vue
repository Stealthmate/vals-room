<template>
  <div>
    <v-data-table
      :items="billsByPerson"
      :headers="headers"
      hide-default-header
      hide-default-footer
      mobile-breakpoint="0"
    >
      <template #[`item.pay`]="{ item }">
        <v-btn @click="pay(item.username)">Pay</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import API from '@/common/api.js';

export default {
  name: 'TheBillContainer',
  data() {
    return {
      orders: []
    };
  },
  computed: {
    billsByPerson() {
      let people = {};
      this.orders.forEach(o => {
        if(!(o.user.username in people)) {
          people[o.user.username] = {
            name: o.user.name,
            bill: 0
          };
        }
        people[o.user.username].bill += o.stars * 100;
      });
      return Object.keys(people).map(k => ({ username: k, ...people[k] }) );
    },
    headers() {
      return [
        { text: 'Name', value: 'name' },
        { text: 'Bill', value: 'bill' },
        { value: 'pay' }
      ]
    }
  },
  created() {
    this.fetch();
  },
  methods: {
    fetch() {
      API.orders.listCompletedOrders().then(response => {
        this.orders = response.data;
      })
    },
    pay(username) {
      let actions = this.orders.filter(o => o.user.username === username).map(o => API.orders.pay(o.id));
      Promise.all(actions).then(() => {
        alert('OK');
      }).catch(err => {
        alert('Error!');
        console.log(err);
      })
    }
  }
}
</script>