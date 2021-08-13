import Vue from 'vue';
import VueRouter from 'vue-router';

import ThePublicWrapper from '@/containers/ThePublicWrapper';
import auth from '@/pages/auth/router.js';

import TheOrdersPage from '@/pages/TheOrdersPage';
import TheUserInvitationsPage from '@/pages/TheUserInvitationsPage';
import TheHomePage from '@/pages/TheHomePage';

import TheAuthWrapper from '@/containers/TheAuthWrapper';

Vue.use(VueRouter);

const internal = [
  {
    path: '',
    name: 'TheHomePage',
    component: TheHomePage
  },
  {
    path: 'orders',
    name: 'TheOrdersPage',
    component: TheOrdersPage
  },
  {
    path: 'invitations',
    name: 'TheUserInvitationsPage',
    component: TheUserInvitationsPage
  }
]

const router = new VueRouter({
  base: '/',
  routes: [
    {
      path: '/auth',
      component: ThePublicWrapper,
      children: auth
    },
    {
      path: '/',
      component: TheAuthWrapper,
      children: internal,
    },
  ]
});

export default router;