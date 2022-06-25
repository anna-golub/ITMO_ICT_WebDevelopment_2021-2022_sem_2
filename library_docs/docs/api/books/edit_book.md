# Редактировать или удалить книгу

**URL** : `books/edit/<int:pk>/`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
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
    "book_reader": []
}
```