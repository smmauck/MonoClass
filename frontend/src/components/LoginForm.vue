<template>
  <v-container
    fluid
    fill-height
  >
    <v-layout
      align-center="true"
      justify-center="true"
    >
      <v-flex
        xs12
        sm8
        md4
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="deep-purple accent-4"
            dark
            flat
          >
            <v-toolbar-title>{{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="Login"
                name="login"
                prepend-icon="mdi-account"
                type="text"
              ></v-text-field>

              <v-text-field
                id="password"
                label="Password"
                name="password"
                prepend-icon="mdi-lock"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="deep-purple accent-4" dark>Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'LoginForm',
  props: {
    title: String,
  },
};
</script>

<style scoped>

</style>
