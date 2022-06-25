from django_filters import rest_framework as filters
from .models import *


class ReaderDateOfBirthFilter(filters.FilterSet):
    class Meta:
        model = Reader
        fields = ['date_of_birth']


class ReaderDateOfBirthRangeFilter(filters.FilterSet):
    date_of_birth = filters.DateFromToRangeFilter()
    ordering = filters.OrderingFilter(
        fields=(
            ('date_of_birth', 'date_of_birth'),
        )
    )

    class Meta:
        model = Reader
        fields = ['date_of_birth']


class BookMainFilter(filters.FilterSet):
    publication_year = filters.RangeFilter()

    genre_options = (
        ('Роман', 'Роман'),
        ('Повесть', 'Повесть'),
        ('Рассказ', 'Рассказ'),
        ('Поэма', 'Поэма'),
        ('Сказка', 'Сказка'),
    )
    genre = filters.MultipleChoiceFilter(choices=genre_options)

    class Meta:
        model = Book
        fields = ['publication_year', 'genre']
