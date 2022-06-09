# Ручные фильтры

## Фильтрация по одному параметру
Фильтрация списка книг по жанру.

```angular2html
class BookFilterView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        return queryset
```

**URL** : `books/filter/?genre=Поэма`

**Content** :
```json
[
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

## Фильтрация по двум параметрам
Фильтрация списка книг по жанру и автору.

```angular2html
class BookFilterView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        author = self.request.query_params.get('author')

        if genre is not None:
            queryset = queryset.filter(genre=genre)
        if author is not None:
            queryset = queryset.filter(authors=author)
        return queryset
```

**URL** : `books/filter/?genre=Роман&author=Л. Толстой`

**Content** :
```json
[
    {
        "id": 1,
        "title": "Война и мир",
        "authors": "Л. Толстой",
        "publisher": "Русская классика",
        "publication_year": 1888,
        "genre": "Роман",
        "book_cypher": "111",
        "book_hall": [
            1
        ],
        "book_reader": [
            2
        ]
    }
]
```

## Фильтрация по двум параметрам и авторизованности пользователя
Фильтрация списка читателей по наличию высшего образования и ученой степени, если пользователь авторизован.

```angular2html
class ReaderFilterView(ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        queryset = Reader.objects.all()

        if self.request.user.is_authenticated:
            education = self.request.query_params.get('education')
            degree = self.request.query_params.get('degree')
            if degree is not None:
                queryset = queryset.filter(degree=degree)
            if education is not None:
                queryset = queryset.filter(education=education)
        return queryset
```

**URL** : `http://localhost:8000/library/readers/filter/?education=Высшее&degree=True`

**Content** : (for an authenticated user)
```json
[
    {
        "id": 12,
        "last_login": "2022-01-18T13:22:09.332248Z",
        "is_superuser": false,
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2022-01-15T22:02:51.909738Z",
        "username": "annaduba",
        "password": "pbkdf2_sha256$260000$fF06owTCgAScvcPsWdYj60$n+aNBVEm7CfVUgLHHH1qdIPi1nUsEEPmQh9yk4FqAUs=",
        "card_number": 333,
        "first_name": "Anna",
        "last_name": "Duba",
        "passport": "1278888888",
        "date_of_birth": "2022-01-04",
        "address": "СПб, Калининский район",
        "phone": "89114765777",
        "education": "Высшее",
        "degree": true,
        "reader_hall": null,
        "groups": [],
        "user_permissions": [],
        "reader_book": [
            3
        ]
    }
]
```