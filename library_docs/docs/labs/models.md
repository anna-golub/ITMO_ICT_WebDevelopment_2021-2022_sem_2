## Book
Книга: 

* title - название
* authors - авторы
* publisher - издательство
* publication year - год издания
* genre - жанр
* book cypher - шифр
* halls (FK) - в каких залах есть эта книга
* readers (FK) - кто сейчас читает эту книгу

## Reader
Читатель (наследуется от `Django` `AbstractUser`): 

* username - логин
* password - пароль
* card number - номер билета
* card number old - старый номер билета  
* first name - имя
* last name - фамилия
* passport - паспорт
* date of birth - дата рождения
* address - адрес
* phone - телефон
* education - образование
* degree - есть ли ученая степень
* hall (FK) - в каком зале находится читатель
* books (FK) - какие книги сейчас читает

## Hall
Зал:

* number - номер
* title - название
* capacity - вместимость

## ReaderBook
Ассоциативная сущность, связывающая книгу и читателя:

* book (FK) - книга
* reader (FK) - читатель
* issue_date - дата выдачи
* due_date - срок возврата

## BookInHall
Ассоциативная сущность, связывающая книгу и зал:

* book (FK) - книга
* hall (FK) - зал
* count - число экземпляров этой книги в этом зале