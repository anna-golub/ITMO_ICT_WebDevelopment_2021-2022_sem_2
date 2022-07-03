from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import *
import os


class Book(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    authors = models.CharField(max_length=1000, verbose_name='Автор(ы)')
    publisher = models.CharField(max_length=500, verbose_name='Издательство')
    publication_year = models.IntegerField(verbose_name='Год издания')
    book_cypher = models.CharField(max_length=50, verbose_name='Шифр')
    book_hall = models.ManyToManyField('Hall', through='BookInHall', verbose_name='Зал')
    book_reader = models.ManyToManyField('Reader', through='ReaderBook', verbose_name='Читатель')

    genre_options = (
        ('Роман', 'Роман'),
        ('Повесть', 'Повесть'),
        ('Рассказ', 'Рассказ'),
        ('Поэма', 'Поэма'),
        ('Сказка', 'Сказка'),
    )
    genre = models.CharField(max_length=300, choices=genre_options, default='-',
                             verbose_name='Жанр', blank=True, null=True)

    def __str__(self):
        return self.title


class Hall(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=500, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')

    def __str__(self):
        return str(self.number) + " - " + self.title


class BookInHall(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Книга')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал')
    count = models.IntegerField(verbose_name='Число экземпляров')

    def __str__(self):
        return str(self.book) + " в зале " + str(self.hall) + ": " + str(self.count)


class Reader(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=300)

    REQUIRED_FIELDS = ['card_number', 'first_name', 'last_name',
                       'passport', 'date_of_birth', 'address', 'phone',
                       'education', 'degree']

    card_number = models.IntegerField(verbose_name='Читательский билет', blank=True, null=True)
    card_number_old = models.IntegerField(verbose_name='Старый читательский билет', blank=True, null=True)

    first_name = models.CharField(max_length=50, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    passport = models.CharField(max_length=10, verbose_name='Паспорт', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    address = models.CharField(max_length=500, verbose_name='Адрес', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='Телефон', blank=True, null=True)

    education_options = (
        ('Среднее общее', 'Среднее общее'),
        ('Среднее специальное', 'Среднее специальное'),
        ('Высшее', 'Высшее'),
        ('Неполное высшее', 'Неполное высшее'),
        ('Неполное среднее', 'Неполное среднее'),
    )
    education = models.CharField(max_length=500, choices=education_options, default='-',
                                 verbose_name='Образование', blank=True, null=True)
    degree = models.BooleanField(default=False, verbose_name='Ученая степень', blank=True, null=True)
    reader_hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал',
                                    blank=True, null=True)
    reader_book = models.ManyToManyField('Book', through='ReaderBook', verbose_name='Книга')

    def __str__(self):
        if self.is_superuser:
            return 'superuser'
        return str(self.last_name) + ' ' + str(self.first_name)


class ReaderBook(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Книга')
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name='Читатель')
    issue_date = models.DateField(verbose_name='Дата выдачи', blank=True, null=True)
    due_date = models.DateField(verbose_name='Дата возврата', blank=True, null=True)

    def __str__(self):
        return str(self.reader) + " : " + str(self.book)


# class ReaderHall(models.Model):
#     reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name='Читатель')
#     hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал')


# class Review(models.Model):
#     review_book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Книга')
#     reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name='Читатель')
#     text = models.CharField(max_length=1000, verbose_name='Текст отзыва', blank=True, null=True)


def get_upload_path(instance, filename):
    return os.path.join('book_covers', str(instance.book), filename)


class BookCover(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Название книги')
    filename = models.CharField(max_length=50, verbose_name='Имя файла', blank=True, null=True)

    file_size = models.IntegerField(verbose_name="Размер файла", blank=True, null=True)
    file = models.FileField(validators=[validate_file_size, validate_file_type],
                            upload_to=get_upload_path
                            )
    filename = file.name

    # file_size = file.size

    def __str__(self):
        return 'Обложка ' + str(self.book)

    def save(self, *args, **kwargs):
        self.file_size = self.file.size
        print('self.book =', self.book)
        super(BookCover, self).save(*args, **kwargs)
