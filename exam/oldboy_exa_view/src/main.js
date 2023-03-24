import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/js/jquery-3.3.1'
import './assets/bootstrap-3.3.7-dist/css/bootstrap.min.css'
import moment from 'moment'
Vue.prototype.$moment = moment

import ElementUi from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import cookies from 'vue-cookies'
import settings from "./assets/js/settings";

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import * as echarts from 'echarts'

Vue.config.productionTip = false

Vue.use(ElementUi)
Vue.prototype.$axios = axios
Vue.prototype.$cookies = cookies
Vue.config.productionTip = false
Vue.prototype.$settings = settings

Vue.prototype.$echarts = echarts

Vue.prototype.$appName = 'My App'


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
