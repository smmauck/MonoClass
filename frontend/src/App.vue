<template>
  <v-app>
    <navigation-bar v-if="!$route.meta.hideNavigation"></navigation-bar>
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue';

export default {
  name: 'App',

  components: {
    NavigationBar,
  },

  data: () => ({
    //
  }),
};
</script>
