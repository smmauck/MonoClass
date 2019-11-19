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
            <v-form
              v-model="valid"
            >
              <v-text-field
                label="IdentiKey"
                name="identikey"
                prepend-icon="mdi-account"
                type="text"
                v-model="username"
                :rules="usernameRules"
                required
                validate-on-blur
              ></v-text-field>

              <v-text-field
                label="Password"
                name="password"
                prepend-icon="mdi-lock"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="showPassword = !showPassword"
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                :rules="passwordRules"
                required
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              class="white--text"
              color="deep-purple accent-4"
              :loading="loading"
              :disabled="!valid"
              @click="login"
            >Login</v-btn>
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
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      showPassword: false,
      valid: false,
      usernameRules: [
        v => !!v || 'IdentiKey is required',
        v => /^[a-z]{4}[0-9]{4}$/.test(v) || 'Invalid IdentiKey format',
      ],
      passwordRules: [
        v => !!v || 'Password is required',
      ],
    };
  },
  methods: {
    login() {
      this.loading = !this.loading;

      const params = new URLSearchParams();
      params.append('username', this.username);
      params.append('password', this.password);

      this.$auth.login({
        data: params.toString(),
        rememberMe: false,
        fetchUser: false,
        redirect: { path: '/about' },
      }).catch(() => {
        // handle error
        this.failedLogin();
      }).finally(() => {
        this.loading = !this.loading;
      });
    },
    failedLogin() {
      this.$toast('Invalid username or password', {
        color: 'error',
        dismissable: true,
        icon: 'mdi-lock-alert',
        closeIcon: 'mdi-close',
        timeout: 5000,
        x: 'center',
        y: 'top',
      });
    },
  },
};
</script>

<style scoped>

</style>
