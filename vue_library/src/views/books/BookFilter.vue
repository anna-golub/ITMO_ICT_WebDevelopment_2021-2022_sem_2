<template>
  <v-container fluid>

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

    <v-data-iterator
      :items="books"
      :items-per-page.sync="itemsPerPage"
      :page.sync="page"
      :search="search"
      :sort-by="sortBy"
      :sort-desc="sortDesc"
      hide-default-footer
    >
      <template v-slot:header>
        <v-toolbar
          dark
          color="blue darken-3"
          class="mb-1"
        >
          <v-text-field
            v-model="search"
            clearable
            flat
            solo-inverted
            hide-details
            prepend-inner-icon="mdi-magnify"
            label="Искать"
            @input="doFilter"
          ></v-text-field>
          <template v-if="$vuetify.breakpoint.mdAndUp">
            <v-spacer></v-spacer>
            <v-select
              v-model="sortBy"
              flat
              solo-inverted
              hide-details
              :items="Object.values(sortProperties)"
              prepend-inner-icon="mdi-magnify"
              label="Упорядочить"
              @change="doFilter"
            ></v-select>
            <v-spacer></v-spacer>
            <v-btn-toggle
              v-model="sortDesc"
              mandatory
            >
              <v-btn
                large
                depressed
                color="blue"
                :value="false"
                @click="doFilter"
              >
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn
                large
                depressed
                color="blue"
                :value="true"
                @click="doFilter"
              >
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </template>
        </v-toolbar>
      </template>

      <v-spacer></v-spacer>

      <template>
        <div>
          <v-container
            class="grey lighten-5 mb-6"
          >
            <v-row
              no-gutters
              style="height: 365px;"
            >
              <v-col
                cols="9"
                sm="6"
                md="8"
              >
                <template>
                  <v-card
                    flat
                    color="transparent"
                  >
                    <p>Год издания</p>

                    <v-card-text>
                      <v-row>
                        <v-col class="px-4" cols="8">
                          <v-range-slider
                            v-model="range"
                            :max="sliderMax"
                            :min="sliderMin"
                            hide-details
                            class="align-center"
                            @change="doFilter"
                          >
                            <template v-slot:prepend>
                              <v-text-field
                                :value="range[0]"
                                class="mt-0 pt-0"
                                hide-details
                                single-line
                                type="number"
                                style="width: 60px"
                                @change="$set(range, 0, $event)"
                              ></v-text-field>
                            </template>
                            <template v-slot:append>
                              <v-text-field
                                :value="range[1]"
                                class="mt-0 pt-0"
                                hide-details
                                single-line
                                type="number"
                                style="width: 60px"
                                @change="$set(range, 1, $event)"
                              ></v-text-field>
                            </template>
                          </v-range-slider>
                        </v-col>
                      </v-row>
                    </v-card-text>
                  </v-card>
                </template>
              </v-col>

              <v-col
                cols="6"
                md="4"
              >
                <template>
                  <v-container fluid>
                    <p>Жанр</p>
                    <v-checkbox
                      v-model="genreSelected"
                      label="Роман"
                      value="Роман"
                      @click="doFilter"
                    ></v-checkbox>
                    <v-checkbox
                      v-model="genreSelected"
                      label="Повесть"
                      value="Повесть"
                      @click="doFilter"
                    ></v-checkbox>
                    <v-checkbox
                      v-model="genreSelected"
                      label="Рассказ"
                      value="Рассказ"
                      @click="doFilter"
                    ></v-checkbox>
                    <v-checkbox
                      v-model="genreSelected"
                      label="Поэма"
                      value="Поэма"
                      @click="doFilter"
                    ></v-checkbox>
                    <v-checkbox
                      v-model="genreSelected"
                      label="Сказка"
                      value="Сказка"
                      @click="doFilter"
                    ></v-checkbox>
                  </v-container>
                </template>

              </v-col>
            </v-row>
          </v-container>
        </div>
      </template>

      <v-spacer></v-spacer>

      <template>
        <v-row>
          <v-col
            v-for="book in books"
            :key="book.title"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card>
              <v-card-title class="subheading font-weight-bold">
                <a @click="goBook(book.id)"> {{ book.title }} </a>
              </v-card-title>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item
                  v-for="(key, index) in bookProperties"
                  :key="index"
                >
                  <v-list-item-content :class="{ 'blue--text': sortBy === key }">
                    {{ key }}:
                  </v-list-item-content>
                  <v-list-item-content
                    class="align-end"
                    :class="{ 'blue--text': sortBy === key }"
                  >
                    {{ book[index] }}
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <template v-slot:footer>
        <v-row
          class="mt-2"
          align="center"
          justify="center"
        >
          <span class="grey--text">Книг на странице</span>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                dark
                text
                color="primary"
                class="ml-2"
                v-bind="attrs"
                v-on="on"
              >
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item
                v-for="(number, index) in itemsPerPageArray"
                :key="index"
                @click="updateItemsPerPage(number)"
              >
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span
            class="mr-4
            grey--text"
          >
            Страница {{ page }} из {{ numberOfPages }}
          </span>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="mr-1"
            @click="formerPage"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="ml-1"
            @click="nextPage"
          >
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
      </template>
    </v-data-iterator>
    <v-card>
      <v-card-text style="margin-top:2cm; font-size:1em">
        <a @click="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'BookFilter',

  data () {
    return {
      authorized: false,
      page: 1,
      itemsPerPage: 2,
      itemsPerPageArray: [2, 3, 4],
      nextPageURL: '',
      formerPageURL: '',
      bookProperties: {
        title: 'Название',
        authors: 'Авторы',
        publisher: 'Издательство',
        publication_year: 'Год издания',
        genre: 'Жанр',
        book_cypher: 'Шифр'
      },
      books: [],
      booksLoaded: false,
      booksTotal: 0,
      keys: [
        'title',
        'authors',
        'publisher',
        'publication_year',
        'genre',
        'book_cypher'
      ],
      search: '',
      sortDesc: false,
      sortBy: '',
      sortProperties: {
        title: 'Название',
        authors: 'Авторы',
        publication_year: 'Год издания'
      },
      sliderMin: 1800,
      sliderMax: 2022,
      range: [1800, 2022],
      genreSelected: []
      // ordering: ''
    }
  },

  created () {
    this.loadBooks()
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  computed: {
    numberOfPages () {
      return Math.ceil(this.booksTotal / this.itemsPerPage)
    },
    ordering () {
      var res = ''
      if (this.sortBy === 'Название') {
        res = 'title'
      }
      if (this.sortBy === 'Авторы') {
        res = 'authors'
      }
      if (this.sortBy === 'Год издания') {
        res = 'publication_year'
      }
      if (this.sortDesc) res = '-' + res
      return res
    }
  },

  methods: {
    async nextPage () {
      if (this.page + 1 <= this.numberOfPages) {
        this.page += 1
        const response = await this.axios.get(this.nextPageURL)
        this.books = response.data.results
        this.page = response.data.current_page
        this.nextPageURL = response.data.next
        this.formerPageURL = response.data.previous
      }
    },

    async formerPage () {
      if (this.page - 1 >= 1) {
        this.page -= 1
        const response = await this.axios.get(this.formerPageURL)
        this.books = response.data.results
        this.nextPageURL = response.data.next
        this.formerPageURL = response.data.previous
      }
    },

    updateItemsPerPage (number) {
      this.itemsPerPage = number
      this.doFilter()
    },

    async loadBooks () {
      this.book_url = 'http://127.0.0.1:8000/library/books/'
      this.book_params = {
        params: {
          page_size: this.itemsPerPage
        }
      }
      const response = await this.axios.get(this.book_url, this.book_params)
      this.books = response.data.results
      this.booksTotal = response.data.count
      this.booksLoaded = true
      this.page = response.data.current_page
      this.nextPageURL = response.data.next
    },

    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },

    async doFilter () {
      console.log('doFilter')
      console.log('this.search =', this.search)
      this.filter_url = 'http://127.0.0.1:8000/library/books/filter/main'

      var params = new URLSearchParams()
      params.append('publication_year_min', this.range[0])
      params.append('publication_year_max', this.range[1])

      if (this.search === null) this.search = ''
      params.append('search', this.search)
      params.append('ordering', this.ordering)

      this.genreSelected.forEach(element => {
        params.append('genre', element)
      })

      params.append('page_size', this.itemsPerPage)
      this.filter_params = {
        params: params
      }
      const response = await this.axios.get(this.filter_url, this.filter_params)
      console.log(response)
      this.books = response.data.results
      this.booksTotal = response.data.count
      this.page = response.data.current_page
      this.nextPageURL = response.data.next
      this.formerPageURL = response.data.previous
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

<style scoped>
</style>
