import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueAuth from '@websanova/vue-auth';
import RouterDriver from '@websanova/vue-auth/drivers/router/vue-router.2.x';
import AxiosDriver from '@websanova/vue-auth/drivers/http/axios.1.x';

const customBearerAuth = {
  request(req, token) {
    if (req.url === 'auth/refresh') {
      // eslint-disable-next-line no-underscore-dangle
      this.options.http._setHeaders.call(this, req, { Authorization: `Bearer ${this.token('refresh_token')}` });
    } else {
      // eslint-disable-next-line no-underscore-dangle
      this.options.http._setHeaders.call(this, req, { Authorization: `Bearer ${token}` });
    }
  },
  response(res) {
    const resData = res.data || {};

    if (typeof resData === 'object') {
      if ('refresh_token' in resData) {
        this.token('refresh_token', resData.refresh_token);
      }
    }

    return resData.access_token;
  },
};

const auth = {
  init() {
    const axiosInstance = axios.create({
      baseURL: '/api/',
    });

    Vue.use(VueAxios, axiosInstance);
    Vue.use(VueAuth, {
      auth: customBearerAuth,
      http: AxiosDriver,
      router: RouterDriver,
      refreshData: {
        url: 'auth/refresh',
        method: 'POST',
        enabled: true,
        interval: 15,
      },
    });
  },
};

export default auth;
