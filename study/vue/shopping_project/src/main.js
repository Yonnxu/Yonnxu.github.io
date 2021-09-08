import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './lib/mui/css/mui.css'
import './lib/mui/css/icons-extra.css'
import auth from './auth.js'
import axios from './axios.js'
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'

Vue.config.productionTip = false

Vue.use(MintUI)
Vue.use(auth)
Vue.use(axios)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
