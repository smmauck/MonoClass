<template>
  <v-app-bar
    color="blue-grey accent-3"
    dark
    app
  >
    <router-link to="/" style="text-decoration:none; color:white">
        <v-toolbar-title>MonoClass</v-toolbar-title>
    </router-link>
    <v-spacer/>
    <v-btn
      v-if="!$auth.check()"
      to="/login"
      outlined
      dark
    >Login</v-btn>
    <template v-else>
      <v-label dark>Welcome, {{ this.$auth.user().identikey }}</v-label>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn
            dark
            v-on="on"
            @click="logout"
            icon
          ><v-icon>mdi-logout</v-icon></v-btn>
        </template >
        <span>Logout</span>
      </v-tooltip>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  name: 'NavigationBar',
  methods: {
    logout() {
      localStorage.removeItem('refresh_token');
      this.$auth.logout({
        makeRequest: false,
        redirect: '/',
      });
    },
  },
};
</script>

<style scoped>

</style>
