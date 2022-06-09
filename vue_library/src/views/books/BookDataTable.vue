<template>
  <div>
    <v-data-table :items="books"
                  :headers="headers">
    </v-data-table>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Каталог библиотеки</h2>
      </v-card-title>
      <v-card-text>
        <ul>
          <li v-for="book in books" :key="book.title">
            {{ book.title }}
          </li>
        </ul>
      </v-card-text>
    </v-card>

  </div>
</template>

<script>

export default {
  name: 'BookDataTable',
  data () {
    return {
      books: ''
    }
  },

  created () {
    this.loadBooks()
  },

  computed: {
    headers () {
      return [
        { text: 'Title', value: 'title' }
      ]
    }
  },

  methods: {
    async loadBooks () {
      this.book_url = 'http://127.0.0.1:8000/library/books/'
      const response = await this.axios.get(this.book_url)
      this.books = response.data
    }
  }
}
</script>

<style>
</style>
