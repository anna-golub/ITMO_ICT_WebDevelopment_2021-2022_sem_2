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
