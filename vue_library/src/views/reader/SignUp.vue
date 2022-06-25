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

    <div class="signup">
      <h2>Регистрация</h2>
      <v-form
        @submit.prevent="signUp"
        ref="signUpForm"
        class="my-2">
        <v-row>
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Логин"
              v-model="signUpForm.username"/>

            <v-text-field
              label="Пароль"
              v-model="signUpForm.password"
              type="password"/>

            <v-text-field
              label="Имя"
              v-model="signUpForm.first_name"
              name="first_name"/>

            <v-text-field
              label="Фамилия"
              v-model="signUpForm.last_name"
              name="last_name"/>

            <v-text-field
              label="Номер билета"
              v-model="signUpForm.card_number"
              name="card_number"
              type="number"/>

            <v-text-field
              label="Дата рождения"
              v-model="signUpForm.date_of_birth"
              name="date_of_birth"
              type="date"/>

            <v-select
              v-model="signUpForm.education"
              :items="educationOptions"
              label="Образование"
            ></v-select>

            <v-checkbox
              v-model="signUpForm.degree"
              :label="'Учёная степень'"
            ></v-checkbox>

            <v-text-field
              label="Паспортные данные"
              v-model="signUpForm.passport"
              name="passport"/>

            <v-text-field
              label="Адрес"
              v-model="signUpForm.address"
              name="address"/>

            <v-text-field
              label="Телефон"
              v-model="signUpForm.phone"
              name="phone"/>

            <v-btn type="submit" color="primary" dark>Зарегистрироваться</v-btn>
          </v-col>
        </v-row>
      </v-form>
      <p class="mt-15">Уже зарегистрированы?
        <router-link to="/library/signin">Войти</router-link>
      </p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'SignUp',

  data: () => ({
    signUpForm: {
      username: '',
      password: '',
      first_name: '',
      last_name: '',
      card_number: '',
      date_of_birth: '',
      education: '',
      degree: '',
      passport: '',
      address: '',
      phone: ''
    },
    educationOptions: ['Среднее общее', 'Среднее специальное',
      'Высшее', 'Неполное высшее', 'Неполное среднее'],
    authorized: false
  }),

  created () {
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async signUp () {
      if (!this.signUpForm.degree) this.signUpForm.degree = false

      try {
        await this.axios.post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        this.$refs.signUpForm.reset()
        await this.$router.push({ name: 'signin' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else if (e.response.data.card_number) {
          alert('Номер билета: ' + e.response.data.card_number)
        } else if (e.response.data.date_of_birth) {
          alert('Дата рождения: ' + e.response.data.date_of_birth)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.degree) {
          alert('Учёная степень: ' + e.response.data.degree)
        } else if (e.response.data.passport) {
          alert('Паспортные данные: ' + e.response.data.passport)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone) {
          alert('Телефон: ' + e.response.data.phone)
        } else {
          console.error(e.message)
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
