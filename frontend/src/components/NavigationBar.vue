<template>
  <v-app-bar
    color="deep-purple accent-4"
    dark
    app
  >
    <v-toolbar-title>MonoClass</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      to="/login"
      outlined
      dark
    >Login</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'NavigationBar',
};
</script>

<style scoped>

</style>
