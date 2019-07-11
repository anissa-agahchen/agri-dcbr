import "./plugins/vuetify";
import "./registerServiceWorker";
import Footer from "./components/Footer";

//import VueKeycloakJs from "@dsb-norge/vue-keycloak-js";
import axios from "axios";
import Vue from "vue";

import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;
// Vue.component(Footer, Footer);

new Vue({
  router,
  //store,
  render: h => h(App)
}).$mount("#app");
