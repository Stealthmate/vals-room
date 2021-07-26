import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.NODE_ENV === 'development' ? 'http://localhost:5000/' : 'https://api.vals-room.top/',
  timeout: 1000,
});
instance.interceptors.request.use(config => {
  let token = window.localStorage.getItem('token');
  config.headers = {
    ...config.headers,
    'Authorization': `Bearer ${token}`
  }
  return config;
});

export default {
  auth: {
    login(username, password) {
      return instance.post('/token/', { username, password });
    },
    getMe() {
      return instance.get('/users/me/');
    }
  },
  getDrinks() {
    return instance.get('/drinks/');
  },
  getTags() {
    return instance.get('/tags/');
  },
  orderItem(name, drink) {
    return instance.post(`/orders/`, { name, drink });
  },
  getOrders() {
    return instance.get(`/orders/`);
  },
  completeOrder(id) { return instance.put(`/orders/${id}/complete/`);},
  cancelOrder(id) { return instance.delete(`/orders/${id}/`);}
}