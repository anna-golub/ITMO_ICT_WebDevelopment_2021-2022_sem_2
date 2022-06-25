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
          <v-text-field
            label="Дата выдачи"
            v-model="submitForm.issue_date"
            name="issue_date"
            type="date"/>
          <v-text-field
            label="Срок возврата"
            v-model="submitForm.due_date"
            name="due_date"
            type="date"/>
        </div>
      </v-card-text>
    </v-card>

    <v-btn color="primary" light @click="takeOutBook">Оформить</v-btn>

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
  name: 'BookTakeOut',

  data: () => ({
    authorized: false,
    book: Object,
    reader: Object,
    submitForm: {
      book: '',
      reader: '',
      issue_date: '',
      due_date: ''
    }
  }),

  created () {
    this.loadReaderData()
    this.loadBook()
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

    async takeOutBook () {
      this.submitForm.book = this.book.id
      this.submitForm.reader = this.reader.id

      if (!localStorage.getItem('auth_token')) {
        await this.$router.push({ name: 'signin' })
      } else {
        await this.axios.post('http://127.0.0.1:8000/library/take_out/', this.submitForm)
        await this.$router.push({ name: 'book', params: { id: this.book.id } })
      }
    },

    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
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
