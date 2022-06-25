<template>
  <div v-if="allLoaded">

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
        <h2>Залы</h2>
      </v-card-title>
      </v-card>
    <v-spacer></v-spacer>

    <v-card
      elevation="2"
      outlined
      class="my-2"
      v-for="hall in halls" v-bind:key="hall.id"
    >
      <v-card-title>
      {{ hall.title }}
        </v-card-title>
      <v-divider></v-divider>
      <v-card-text style="font-size:1em">
        <ul>
          <li v-for="book_in_hall in book_in_halls[hall.id]" :key="book_in_hall.id">
            <a @click="goBook(book_in_hall.book.id)">{{ book_in_hall.book.title }}</a> -
            {{ book_in_hall.book.authors }}
            ({{book_in_hall.count}} шт.)
            <v-spacer></v-spacer>
          </li>
        </ul>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:2cm; font-size:1em">
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'HallList',
  data () {
    return {
      books: '',
      halls: {},
      book_in_halls: {},
      allLoaded: false,
      authorized: true
    }
  },

  created () {
    this.loadHalls()
    this.loadBookInHalls()

    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    async loadHalls () {
      this.halls_url = 'http://127.0.0.1:8000/library/halls/'
      const response = await this.axios.get(this.halls_url)
      this.halls = response.data
    },

    async loadBookInHalls () {
      this.book_in_halls_url = 'http://127.0.0.1:8000/library/book_in_halls/'
      const response = await this.axios.get(this.book_in_halls_url)

      for (const value of response.data) {
        if (!(value.hall in this.book_in_halls)) {
          this.book_in_halls[value.hall] = []
        }
        this.book_in_halls[value.hall].push(value)
      }

      this.allLoaded = true
    },

    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
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
