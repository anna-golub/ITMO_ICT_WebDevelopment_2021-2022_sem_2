<template>
  <div>

    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Добро пожаловать в библиотеку!</h2>
      </v-card-title>
    </v-card>

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
      <v-card-text>
        <h3><a @click="goCatalogue">Каталог</a></h3>
      </v-card-text>
    </v-card>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-text>
        <h3><a @click="goHalls">Залы</a></h3>
      </v-card-text>
    </v-card>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-text>
        <h3>
          <a v-if="this.authorized" @click="goProfile">Личный кабинет</a>
          <a v-else @click="goSignIn">Войти</a>
        </h3>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'Home',

  data: () => ({
    authorized: false,
    navigationItems: [
      { title: 'Домашняя страница', icon: 'mdi-view-dashboard' },
      { title: 'Каталог', icon: 'mdi-book-search-outline', click: 'goCatalogue' },
      { title: 'Залы', icon: 'mdi-bookshelf' },
      { title: 'Книга (пример)', icon: 'mdi-book' },
      { title: 'Взять книгу (пример)', icon: 'mdi-book-plus' },
      { title: 'Вернуть книгу (пример)', icon: 'mdi-book-minus' },
      { title: 'Регистрация', icon: 'mdi-account-plus' },
      { title: 'Вход', icon: 'mdi-login' },
      { title: 'Личный кабинет', icon: 'mdi-account' },
      { title: 'Редактировать информацию', icon: 'mdi-account-edit' }
    ]
  }),

  created () {
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
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
    },

    navigate (icon) {
      switch (icon.title) {
        case 'Домашняя страница':
          this.goHome()
          break
        case 'Каталог':
          this.goCatalogue()
          break
        case 'Залы':
          this.goHalls()
          break
        case 'Книга (пример)':
          this.goBookExample()
          break
        case 'Взять книгу (пример)':
          this.goTakeOutExample()
          break
        case 'Вернуть книгу (пример)':
          this.goReturnExample()
          break
        case 'Регистрация':
          this.goSignUp()
          break
        case 'Вход':
          this.goSignIn()
          break
        case 'Личный кабинет':
          this.goProfile()
          break
        case 'Редактировать информацию':
          this.goProfileEdit()
          break
      }
    }
  }
}
</script>
