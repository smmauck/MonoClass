<template>
  <v-app>
    <navigation-bar v-if="!$route.meta.hideNavigation"/>
    <v-content>
      <v-container fluid style="height:100%">
        <div v-if="$auth.ready()">
          <router-view/>
        </div>

        <div v-else style="text-align:center">
            <v-progress-circular
                :size="50"
                indeterminate
                color="primary"
            >
            </v-progress-circular>
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
