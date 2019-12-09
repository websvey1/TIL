import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import VueResource from 'vue-resource'
import feather from 'vue-icon'

import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'

import axios from 'axios'

import VueSession from 'vue-session'
import VModal from 'vue-js-modal'

import { store } from './store'

Vue.config.productionTip = false
Vue.use(VModal, { dynamic: true });

Vue.use(Vuetify, {
	iconfont: 'fa',
	theme: {
		primary: '#3f51b5',
		secondary: '#b0bec5',
		accent: '#8c9eff',
		error: '#b71c1c'
	}
})

Vue.use(VueSession)

Vue.use(VueResource);
Vue.use(feather,'v-icon');
Vue.use(VueSimplemde)
Vue.prototype.$axios = axios

new Vue({
  router,
	store,
  render: h => h(App),
}).$mount('#app')
