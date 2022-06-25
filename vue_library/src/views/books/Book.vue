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
        <h2>{{ this.book.title }}</h2>
      </v-card-title>

      <v-card-text style="font-size:1em">
        <div class="text--primary">
          Авторы: <b>{{ this.book.authors }}</b> <br>
          Жанр: {{ this.book.genre }} <br>
          Год издания: {{ this.book.publication_year }} <br>
          Издательство: {{ this.book.publisher }} <br>
          Библиотечный номер: {{ this.book.book_cypher }} <br>
          <br>
          Залы:
          <ul>
            <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">
              {{ hall.title }}
            </li>
          </ul>
<!--          <br>-->
<!--          Сейчас читают: <span v-if="!this.book.book_reader.length">-</span>-->
<!--          <ul v-else>-->
<!--            <li v-for="reader in this.book.book_reader" v-bind:key="reader" v-bind:reader="reader">-->
<!--              {{ reader.first_name }} {{ reader.last_name }}-->
<!--            </li>-->
<!--          </ul>-->
        </div>
      </v-card-text>
    </v-card>

    <v-btn v-if="!this.bookOnHold" color="primary" light @click="takeOutBook">Хочу прочитать</v-btn>

    <v-card
      elevation="2"
      outlined
      class="my-2"
      v-else>
      <v-card-text style="font-size: 1em">
        <div class="text--primary">Вы сейчас читаете эту книгу</div>
        <a @click="returnBook">Вернуть книгу в библиотеку</a>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:2cm; font-size:1em">
        <a @click.prevent="goCatalogue">Каталог</a><br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'Book',
  data () {
    return {
      authorized: false,
      book: Object,
      reader: Object,
      bookOnHold: false,
      bookReaderID: ''
    }
  },
  created () {
    this.loadBook()
    this.loadReaderData()
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async loadBook () {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await this.axios.get(this.book_url)
      this.book = response.data
    },

    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.checkOnHold()
    },

    async checkOnHold () {
      this.reader_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await this.axios.get(this.reader_url)
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data.reader_book)) {
        if (value.id === this.book.id) {
          this.bookOnHold = true
          // this.bookReaderID = value.
          break
        }
      }
    },

    takeOutBook () {
      this.$router.push({ name: 'take_out', params: { id: this.book.id } })
    },

    async returnBook () {
      const response = await this.axios.get('http://127.0.0.1:8000/library/reader_books/')

      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data)) {
        if (value.reader.id === this.reader.id && value.book.id === this.book.id) {
          this.bookReaderID = value.id
          break
        }
      }
      await this.$router.push({ name: 'return', params: { id: this.bookReaderID } })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHome () {
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
