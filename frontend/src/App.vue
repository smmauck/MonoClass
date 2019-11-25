<template>
  <v-app>
    <navigation-bar v-if="!$route.meta.hideNavigation && $auth.ready()"/>
    <v-content>
      <v-container fluid>
        <div v-if="$auth.ready()">
          <router-view/>
        </div>

        <div v-else>
          Loading ...
        </div>
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
