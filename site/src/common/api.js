import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.NODE_ENV === 'development' ? 'http://localhost:5000/' : 'https://api.vals-room.top/',
  timeout: 1000,
});
instance.interceptors.request.use(config => {
  let token = window.localStorage.getItem('token');
  config.headers = {
    ...config.headers,
    'Authorization': token ? `Bearer ${token}` : undefined
  }
  return config;
});
instance.interceptors.response.use(undefined, error => {
  if(error.response && error.response.status === 401) {
    window.localStorage.removeItem('token');
  }
  return error;
})

export default {
  auth: {
    register(invitation, username, password, name) {
      return instance.post('/users/register/', { invitation: parseInt(invitation), username, password, name });
    },
    login(username, password) {
      return instance.post('/token/', { username, password });
    },
    getMe() {
      return instance.get('/users/me/');
    }
  },
  admin: {
    listInvitations() {
      return instance.get('/admin/invitations/');
    },
    createInvitation() {
      return instance.post('/admin/invitations/');
    },
    deleteInvitation(no) {
      return instance.delete(`/admin/invitations/${no}/`);
    }
  },
  drinks: {
    getAll() { return instance.get('/drinks/'); }
  },
  orders: {
    listActiveOrders() { return instance.get('/orders/'); },
    listCompletedOrders() { return instance.get('/orders/completed/'); },
    listUserOrders() { return instance.get('/orders/user/'); },
    place(drink) { return instance.post(`/orders/`, { drink }); },
    cancel(order_id) { return instance.delete(`/orders/${order_id}/`); },
    complete(order_id) { return instance.post(`/orders/${order_id}/complete/`); },
    pay(order_id) { return instance.post(`/orders/${order_id}/pay/`); },
  },
  getTags() {
    return instance.get('/tags/');
  },
}