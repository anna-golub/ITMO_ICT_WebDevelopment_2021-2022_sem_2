Эндпойнты предоставляются библиотекой `djoser`.
Пользователи (читатели) авторизуются по логину и паролю.
Им выдается токен аутентификации и в дальнейшем они аутентифицируются по нему.

## Получение токена

**URL** : `/auth/token/login`

**Method** : `POST`

Success Responses:

**Code** : `201 Created`

**Content** : 

```
{
    "auth_token": "bfbfea964"
}
```

## Текущий пользователь

Эндпойнт для просмотра или редактирования информации о текущем авторизованном пользователе.

**URL** : `/auth/users/me`

**Method** : `GET`

Success Responses:

**Code** : `200 OK`

**Content** : 

```
{
    "card_number": 333,
    "first_name": "Anna",
    "last_name": "Duba",
    "passport": "1278888888",
    "date_of_birth": "2002-01-04",
    "address": "СПб, Калининский район",
    "phone": "89114765777",
    "education": "Высшее",
    "degree": true,
    "id": 12,
    "username": "annaduba"
}
```