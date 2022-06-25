# Список экземпляров BookInHall

**URL** : `book_in_halls/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "book": {
            "id": 1,
            "title": "Война и мир",
            "authors": "Л. Толстой",
            "publisher": "Русская классика",
            "publication_year": 1888,
            "book_cypher": "111",
            "genre": "Роман",
            "book_hall": [
                1
            ],
            "book_reader": [
                3,
                2
            ]
        },
        "count": 3,
        "hall": 1
    },
    {
        "id": 2,
        "book": {
            "id": 2,
            "title": "Янки при дворе короля Артура",
            "authors": "Марк Твен",
            "publisher": "Зарубежная классика",
            "publication_year": 1910,
            "book_cypher": "222",
            "genre": "Роман",
            "book_hall": [
                2
            ],
            "book_reader": [
                22
            ]
        },
        "count": 2,
        "hall": 2
    }
]
```