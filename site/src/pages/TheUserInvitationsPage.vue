<template>
  <app-page>
    <v-data-table
      :items="invitations"
      :headers="headers"
      hide-default-footer
      hide-default-header
      mobile-breakpoint="0"
    >
      <template #[`item.action`]="{ item }">
        <v-btn icon @click="remove(item.no)"><v-icon>mdi-delete</v-icon></v-btn>
      </template>
    </v-data-table>
    <v-btn @click="create">Generate</v-btn>

    <SnackbarAlert ref="snackbar" />
  </app-page>
</template>

<script>

import API from '@/common/api.js';

export default {
  name: 'TheUserInvitationsPage',
  data() {
    return {
      invitations: []
    }
  },
  computed: {
    headers() {
      return [
        { text: 'No', value: 'no' },
        { text: 'Action', value: 'action' }
      ];
    }
  },
  created() {
    this.fetch();
  },
  methods: {
    fetch() {
      API.admin.listInvitations().then(response => {
        this.invitations = response.data;
      }).catch(err => {
        this.$refs.snackbar.error('Error!');
      });
    },
    create() {
      API.admin.createInvitation().then(response => {
        this.fetch();
      }).catch(err => {
        this.$refs.snackbar.error('Error!');
      });
    },
    remove(no) {
      API.admin.deleteInvitation(no).then(response => {
        this.fetch();
      }).catch(err => {
        this.$refs.snackbar.error('Error!');
      });
    }
  }
}
</script>