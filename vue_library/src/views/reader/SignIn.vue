<template>

  <div>

    <v-navigation-drawer
      app
      permanent>
      <v-list
        dense
        nav
      >
        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon @click="goHome">mdi-view-dashboard</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title @click="goHome">Домашняя страница</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon @click="goCatalogue">mdi-book-search-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title @click="goCatalogue">Каталог</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon @click="goHalls">mdi-bookshelf</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title @click="goHalls">Залы</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon v-if="authorized" @click="goProfile">mdi-account</v-icon>
            <v-icon v-else @click="goSignIn">mdi-login</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-if="authorized" @click="goProfile">Личный кабинет</v-list-item-title>
            <v-list-item-title v-else @click="goSignIn">Войти</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <div class="signIn">
      <h2>Авторизация</h2>
      <v-form
        @submit.prevent="signIn"
        ref="signInForm"
        class="my-2">
        <v-row>
          <v-col cols="3" class="mx-auto">
            <v-text-field
              label="Логин"
              v-model="signInForm.username"/>
            <v-text-field
              label="Пароль"
              v-model="signInForm.password"
              type="password"/>
            <v-btn type="submit" color="primary" dark>Войти</v-btn>
          </v-col>
        </v-row>
      </v-form>
      <p class="mt-15">Ещё нет аккаунта?<br>
        <router-link to="/library/signup">Зарегистрироваться</router-link>
      </p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'SignIn',

  data: () => ({
    signInForm: {
      username: '',
      password: ''
    },
    authorized: false
  }),

  created () {
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async signIn () {
      try {
        const response = await this.axios.post('http://127.0.0.1:8000/auth/token/login', this.signInForm)
        this.$refs.signInForm.reset()
        localStorage.setItem('auth_token', response.data.auth_token)
        await this.$router.push({ name: 'home' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert('Неверный логин или пароль.')
        } else if (e.response.data.password || e.response.data.username) {
          alert('Поля "логин" и "пароль" должны быть заполнены.')
        } else {
          console.error('API error:', e.message)
        }
      }
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHalls () {
      this.$router.push({ name: 'halls' })
    },

    goProfile () {
      this.$router.push({ name: 'reader_profile' })
    },

    goSignIn () {
      this.$router.push({ name: 'signin' })
    }
  }
}
</script>

<style>
</style>
