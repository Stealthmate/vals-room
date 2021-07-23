import Vue from 'vue';
import VueRouter from 'vue-router';

import TheCocktailsPage from '@/pages/TheCocktailsPage';
import TheAuthWrapper from '@/containers/TheAuthWrapper';
import TheLoginPage from '@/pages/TheLoginPage';
import TheOrdersPage from '@/pages/TheOrdersPage';

Vue.use(VueRouter);

const internal = [
  {
    path: '/',
    name: 'TheHomePage',
    redirect: TheCocktailsPage
  },
  {
    path: '/menu',
    name: 'TheCocktailsPage',
    component: TheCocktailsPage
  },
  {
    path: '/orders',
    name: 'TheOrdersPage',
    component: TheOrdersPage
  }
]

export default new VueRouter({
  base: '/vals-room',
  routes: [
    {
      path: '/login',
      name: 'TheLoginPage',
      component: TheLoginPage
    },
    {
      path: '/',
      component: TheAuthWrapper,
      children: internal
    },
  ]
});