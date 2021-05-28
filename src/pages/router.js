import Vue from 'vue';
import VueRouter from 'vue-router';

import TheCocktailsPage from '@/pages/TheCocktailsPage';
import TheBottlesPage from '@/pages/TheBottlesPage';

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Home',
      redirect: { name: 'TheCocktailsPage' }
    },
    { 
      path: '/cocktails', 
      name: 'TheCocktailsPage',
      component: TheCocktailsPage 
    },
    { 
      path: '/bottles', 
      name: 'TheBottlesPage',
      component: TheBottlesPage 
    },
  ]
});