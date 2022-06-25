from django.urls import path, re_path

from .views import *

app_name = "library_app"

urlpatterns = [
    path('books/', BookListAPIView.as_view()),  # list of books
    path('books/create/', BookCreateAPIView.as_view(), name='books_create'),  # create book
    path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='books_retrieve'),  # book info by id

    re_path('^books/filter/$', BookFilterView.as_view()),  # books filtered by genre (and author)

    # search books by title and author
    path('books/filter/search/', BookSearchView.as_view(), name='books_search'),
    path('books/filter/main/', BookMainFilterView.as_view()),  # main book filter

    # update / delete book by id
    path('books/edit/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='books_edit'),

    path('readers/', ReaderListAPIView.as_view()),  # list of readers
    path('readers/create/', ReaderCreateAPIView.as_view(), name='readers_create'),  # create reader
    path('readers/<int:pk>/', ReaderRetrieveAPIView.as_view(), name='readers_retrieve'),  # reader info by id

    # readers filtered by education and degree if authenticated
    re_path(r'^readers/filter/$', ReaderFilterView.as_view()),

    # readers with given date of birth
    path('readers/filter/date_of_birth/', ReaderDateOfBirthFilterView.as_view()),

    # readers with date of birth in given range
    path('readers/filter/date_of_birth-range/', ReaderDateOfBirthRangeFilterView.as_view()),

    # update / delete reader by id
    path('readers/edit/<int:pk>/', ReaderRetrieveUpdateDestroyAPIView.as_view(), name='readers_edit'),

    # path('report/', ReportApiView.as_view()),  # report

    path('take_out/', ReaderBookCreateAPIView.as_view(), name='take_out'),  # take out book
    path('return/<int:pk>/', ReaderBookRetrieveUpdateDestroyAPIView.as_view(), name='return'),  # return book
    path('reader_books/', ReaderBookListAPIView.as_view()),  # list of reader_book's
    # reader_book info
    path('reader_books/<int:pk>/', ReaderBookRetrieveAPIView.as_view(), name='reader_books_retrieve'),

    # filter ReaderBooks by book author
    path('reader_books/filter/', ReaderBookAuthorView.as_view()),

    # book cover upload
    path('book_cover_upload/', BookCoverCreateView.as_view()),
    path('book_cover_multiple/', BookCoverMultipleView.as_view()),

    # review
    # path('reviews/', ReviewListView.as_view()),
    # path('reviews/create/', ReviewCreateView.as_view()),

    # halls
    path('halls/', HallListAPIView.as_view()),
    path('book_in_halls/', BookInHallListAPIView.as_view()),
]
