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
        </div>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:2cm; font-size:1em">
        <div class="text--primary">
          Дата выдачи: {{ this.issue_date }} <br>
          Срок возврата: {{ this.due_date }}
        </div>
      </v-card-text>
    </v-card>

    <v-btn style="margin-top:0.5cm" color="primary" light @click="returnBook">Вернуть</v-btn>

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
  name: 'BookReturn',

  data: () => ({
    authorized: false,
    book: Object,
    reader: Object,
    issue_date: '',
    due_date: ''
  }),

  created () {
    this.loadReaderBookData()
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async loadReaderBookData () {
      this.book_url = 'http://127.0.0.1:8000/library/reader_books/' + this.$route.params.id
      const response = await this.axios.get(this.book_url)
      this.book = response.data.book
      this.reader = response.data.reader
      this.issue_date = response.data.issue_date
      this.due_date = response.data.due_date
    },

    async returnBook () {
      this.return_url = 'http://127.0.0.1:8000/library/return/' + this.$route.params.id
      await this.axios.delete(this.return_url)
      alert('Вы вернули книгу в библиотеку')
      await this.$router.push({ name: 'catalogue' })
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
