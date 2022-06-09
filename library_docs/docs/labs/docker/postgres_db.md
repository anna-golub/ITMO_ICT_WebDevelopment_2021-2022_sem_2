# Создание пользователя postgres

Чтобы перенести таблицы в `postgres`, выполняем команду `python manage.py migrate`.

![Screenshot](img/postgres_migrate.png "Screenshot")
![Screenshot](img/pgadmin_tables.png "Screenshot")

Для создания нового пользователя в командной строке `postgres` выполняются следующие команды:  
1. `create user library_user with encrypted password 'librarypwd';`  
2. `grant all privileges on database library_db to library_user;`

![Screenshot](img/new_user_postgres_1.png "Screenshot")
![Screenshot](img/new_user_postgres_2.png "Screenshot")
