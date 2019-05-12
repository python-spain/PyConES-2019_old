// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import VueI18n from 'vue-i18n';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import BootstrapVue from 'bootstrap-vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import messages from './translations';
import axios from 'axios';

require('../static/css/styles.css')
library.add(fas, fab);

Vue.prototype.$eventBus = new Vue()
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false;

Vue.use(BootstrapVue)
Vue.use(VueI18n)

let lang = navigator.language.substr(0,2)
if(lang !== 'es' &&  lang !== 'en'){
    lang = 'es';
}
const i18n = new VueI18n({
    locale: lang,
    messages,
})


/* eslint-disable no-new */
new Vue({
  i18n,
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});

