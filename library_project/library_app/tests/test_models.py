from django.test import TestCase

from ..models import *


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='Аэлита',
            authors='А. Толстой',
            publisher='Русская литература',
            publication_year=1956,
            genre='Фантастика',
            book_cypher='97',
            # book_hall=1,
            # book_reader=1
        )

    def test_book_publisher_label(self):
        obj = Book.objects.get(id=1)
        field_label = obj._meta.get_field('publisher').verbose_name
        self.assertEquals(field_label, 'Издательство')


class ReaderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Reader.objects.create(
            card_number=111,
            first_name='Lina',
            last_name='Anil',
            passport='1111111111',
            date_of_birth='1990-09-09',
            address='...',
            phone='89111111111',
            education='Среднее общее',
            degree=False
        )

    def test_passport_max_length(self):
        obj = Reader.objects.get(id=1)
        max_length = obj._meta.get_field('passport').max_length
        self.assertEquals(max_length, 10)


class ReaderBookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='Аэлита',
            authors='А. Толстой',
            publisher='Русская литература',
            publication_year=1956,
            genre='Фантастика',
            book_cypher='97',
            # book_hall=1,
            # book_reader=1
        )

        Reader.objects.create(
            first_name='Lina',
            last_name='Anil',
            passport='1111111111',
            card_number=111,
            date_of_birth='1990-09-09',
            address='...',
            phone='89111111111',
            education='Среднее общее',
            degree=False
        )

        ReaderBook.objects.create(
            book=Book.objects.get(id=1),
            reader=Reader.objects.get(id=1),
            issue_date='2006-06-23',
            due_date='2006-07-08'
        )

    def test_object_name_is_name(self):
        obj = ReaderBook.objects.get(id=1)
        expected_object_name = str(obj.reader) + " : " + str(obj.book)
        self.assertEquals(str(obj), expected_object_name)
