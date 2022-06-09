# Автоматические фильтры

## Фильтрация по дате
Фильтрация читателей по заданной дате рождения.

`filters.py`

```angular2html
class ReaderDateOfBirthFilter(filters.FilterSet):
    class Meta:
        model = Reader
        fields = ['date_of_birth']
```

`views.py`

```angular2html
class ReaderDateOfBirthFilterView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReaderDateOfBirthFilter
```

**URL** : `/readers/filter/date_of_birth/`

**Content** :

```json
[
    {
        "id": 2,
        "last_login": null,
        "is_superuser": false,
        "email": "",
        "is_staff": false,
        "is_active": false,
        "date_joined": "2021-12-08T11:50:26.300755Z",
        "username": "alina",
        "password": "11r11",
        "card_number": 1,
        "first_name": "Alina",
        "last_name": "Ivanova",
        "passport": "1111111111",
        "date_of_birth": "2000-10-10",
        "address": "г. Санкт-Петербург",
        "phone": "89111111111",
        "education": "Высшее",
        "degree": false,
        "reader_hall": 1,
        "groups": [],
        "user_permissions": [
            20
        ],
        "reader_book": [
            1
        ]
    }
]
```

## Поиск по двум полям
Поиск подстроки в названии и имени автора книги.

`views.py`

```angular2html
class BookSearchView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title', 'authors']
```

**URL** : `/books/filter/search/`

**Content** :

```json
[
    {
        "id": 2,
        "title": "Янки при дворе короля Артура",
        "authors": "Марк Твен",
        "publisher": "Зарубежная классика",
        "publication_year": 1910,
        "genre": "Приключенческий роман",
        "book_cypher": "222",
        "book_hall": [
            2
        ],
        "book_reader": []
    },
    {
        "id": 3,
        "title": "Евгений Онегин",
        "authors": "А. Пушкин",
        "publisher": "Русская классика",
        "publication_year": 1957,
        "genre": "Поэма",
        "book_cypher": "444",
        "book_hall": [
            1
        ],
        "book_reader": [
            1,
            1,
            12
        ]
    }
]
```

## Поиск по полям связанной таблицы
Поиск по названию книги среди записей о выдаче книги читателю.

`views.py`

```angular2html
class ReaderBookAuthorView(ListAPIView):
    queryset = ReaderBook.objects.all()
    serializer_class = ReaderBookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('book__title',)
```

**URL** : `/reader_books/filter/`

**Content** :

```json
[
    {
        "id": 3,
        "reader": {
            "id": 1,
            "first_name": "Анна",
            "last_name": "Голуб"
        },
        "issue_date": "2020-02-23",
        "due_date": "2020-02-23",
        "book": 3
    },
    {
        "id": 5,
        "reader": {
            "id": 12,
            "first_name": "Anna",
            "last_name": "Duba"
        },
        "issue_date": "2020-02-23",
        "due_date": "2020-02-23",
        "book": 3
    }
]
```

## Фильтрация в диапазоне дат и сортировка

Отбираются читатели, дата рождения которых находится в заданном диапазоне. Полученный список сортируется по возрастанию
даты рождения.

`filters.py`

```angular2html
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

```

`views.py`

```angular2html
class ReaderDateOfBirthFilterView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReaderDateOfBirthFilter
```

**URL** : `/readers/filter/date_of_birth-range/`

**Content** :

```json
[
  {
    "id": 2,
    "first_name": "Alina",
    "last_name": "Ivanova",
    "date_of_birth": "2000-10-10"
  },
  {
    "id": 3,
    "first_name": "Ivan",
    "last_name": "Petrov",
    "date_of_birth": "2001-03-03"
  },
  {
    "id": 12,
    "first_name": "Anna",
    "last_name": "Duba",
    "date_of_birth": "2002-01-04"
  }
]
```