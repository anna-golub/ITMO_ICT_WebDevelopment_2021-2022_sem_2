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

    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Личный кабинет</h2>
      </v-card-title>

      <v-card-text style="font-size:1em">
        <div class="text--primary">
          Имя: <b>{{ this.reader.first_name }}</b> <br>
          Фамилия: <b>{{ this.reader.last_name }}</b> <br>
          Логин: {{ this.reader.username }} <br>
          Номер билета: {{ this.reader.card_number }} <br>
          Дата рождения: {{ this.reader.date_of_birth }} <br>
          Образование: {{ this.reader.education }} <br>
          Ученая степень: {{ this.reader.degree ? 'есть' : 'нет' }} <br>
          Паспортные данные: {{ this.reader.passport }} <br>
          Адрес: {{ this.reader.address }} <br>
          Телефон: {{ this.reader.phone }} <br>
        </div>
      </v-card-text>
    </v-card>

    <v-card
      elevation="2"
      outlined
      class="my-2">
      <v-card-text class="text--primary" style="font-size:1em">
        Вы сейчас читаете:
        <ul>
          <li v-for="book in reader.reader_book" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>, {{ book.authors }}
          </li>
        </ul>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:1cm; font-size:1em">
        <a @click.prevent="goEdit">Редактировать профиль</a><br>
        <a @click.prevent="SignOut">Выйти</a><br>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:1cm; font-size:1em">
        <a @click.prevent="goCatalogue">Каталог</a><br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'ReaderProfile',

  data () {
    return {
      reader: Object,
      authorized: false
    }
  },

  created () {
    this.loadReaderData()
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.loadCurrentlyReading()
    },

    async loadCurrentlyReading () {
      this.cur_read_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await this.axios.get(this.cur_read_url)
      this.reader = response.data
    },

    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goEdit () {
      this.$router.push({ name: 'reader_profile_edit' })
    },

    SignOut () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'home' })
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
