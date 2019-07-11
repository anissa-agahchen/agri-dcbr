<template>
  <v-app>
    <div id="app">
      <Navbar />
      <div id="nav">
        <router-link to="/">AGRI site</router-link>|
        <router-link to="/preamble">Preamble</router-link>|
        <router-link to="/register">Registration</router-link>|
        <router-link to="/payment">Payment</router-link>|
        <router-link to="/review">Review</router-link>|
        <router-link to="/confirmation">Confirmation</router-link>
        <br />
        <br />
        <!-- <button @click="$keycloak.logoutFn" v-if="$keycloak.authenticated">Log out</button> -->
      </div>
      <router-view />
    </div>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default {
  components: {
    Navbar,
    Footer
  }
};
</script>


<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>