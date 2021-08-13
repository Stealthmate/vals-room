
import TheAuthPage from '@/pages/auth/TheAuthPage';
import TheLoginPage from '@/pages/auth/TheLoginPage';
import TheRegisterPage from '@/pages/auth/TheRegisterPage';

export default [
  {
    path: '',
    name: 'TheAuthPage',
    component: TheAuthPage
  },
  {
    path: 'login',
    name: 'TheLoginPage',
    component: TheLoginPage
  },
  {
    path: 'register',
    name: 'TheRegisterPage',
    component: TheRegisterPage
  },
];