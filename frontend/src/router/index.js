import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import Dashboard from '@/views/Dashboard.vue';
import Class from '@/views/Class.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: 'Home',
    },
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      auth: false,
      hideNavigation: true,
      title: 'Login',
    },
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    meta: {
      auth: true,
      title: 'Dashboard',
    },
  },
  {
    path: '/class/:classid/:classsource',
    name: 'class',
    component: Class,
    meta: {
      auth: true,
      title: 'Class View',
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
