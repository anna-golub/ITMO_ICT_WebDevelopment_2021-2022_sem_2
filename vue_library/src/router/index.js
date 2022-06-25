import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home'
// import BookList from '@/views/books/BookList'
import Book from '@/views/books/Book'
import BookTakeOut from '@/views/books/BookTakeOut'
import BookReturn from '@/views/books/BookReturn'
import SignUp from '@/views/reader/SignUp'
import SignIn from '@/views/reader/SignIn'
import ReaderProfile from '@/views/reader/ReaderProfile'
import ReaderProfileEdit from '@/views/reader/ReaderProfileEdit'
import BookFilter from '@/views/books/BookFilter'
import HallList from '@/views/books/HallList'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/library/home',
      name: 'home',
      component: Home
    },
    {
      path: '/library/books',
      name: 'catalogue',
      component: BookFilter
    },
    {
      path: '/library/books/:id',
      name: 'book',
      component: Book
    },
    {
      path: '/library/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/library/signin',
      name: 'signin',
      component: SignIn
    },
    {
      path: '/library/profile',
      name: 'reader_profile',
      component: ReaderProfile
    },
    {
      path: '/library/profile/edit',
      name: 'reader_profile_edit',
      component: ReaderProfileEdit
    },
    {
      path: '/library/take_out/',
      name: 'take_out',
      component: BookTakeOut
    },
    {
      path: '/library/return/:id',
      name: 'return',
      component: BookReturn
    },
    {
      path: '/library/halls/',
      name: 'halls',
      component: HallList
    }
  ]
})
