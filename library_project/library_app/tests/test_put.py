from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import *

import datetime


class BookUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='Аэлита',
            authors='А. Толстой',
            publisher='Русская литература',
            publication_year=1956,
            genre='Фантастика',
            book_cypher='97'
        )

    def test_update_book(self):
        self.maxDiff = None

        url = reverse('library_app:books_edit', args=['1'])

        data = {'id': 1,
                'title': 'Аэлита',
                'authors': 'А. Толстой',
                'publisher': 'Русская литература',
                'publication_year': 1956,
                'genre': 'Фантастика',
                'book_cypher': '97',
                'book_hall': [],
                'book_reader': []
                }

        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)

        data['book_cypher'] = '97a'

        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)


class ReaderUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Reader.objects.create(
            username='newuser',
            password='userpwd',
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

    def test_update_reader(self):
        self.maxDiff = None

        url = reverse('library_app:readers_edit', args=['1'])
        today = str(datetime.date.today())

        data = {
            'id': 1,
            'last_login': None,
            'is_superuser': False,
            'email': '',
            'is_staff': False,
            'is_active': True,
            'date_joined': today,
            'username': 'newuser',
            'password': 'userpwd',
            'card_number': 111,
            'card_number_old': None,
            'first_name': 'Lina',
            'last_name': 'Anil',
            'passport': '1111111111',
            'date_of_birth': '1990-09-09',
            'address': '...',
            'phone': '89111111111',
            'education': 'Среднее общее',
            'degree': False,
            'reader_hall': None,
            'groups': [],
            'user_permissions': [],
            'reader_book': []
        }

        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        response_data = response_retrieve.json()
        response_data['date_joined'] = response_data['date_joined'][:10]
        self.assertEqual(response_data, data)

        data['passport'] = '2222222222'

        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        response_data = response_update.json()
        response_data['date_joined'] = response_data['date_joined'][:10]
        self.assertEqual(response_data, data)


class ReaderBookUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='Аэлита',
            authors='А. Толстой',
            publisher='Русская литература',
            publication_year=1956,
            genre='Фантастика',
            book_cypher='97'
        )

        Reader.objects.create(
            username='newuser',
            password='userpwd',
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
            id=1,
            issue_date="1987-03-12",
            due_date="1987-04-12",
            book=Book.objects.get(id=1),
            reader=Reader.objects.get(id=1),
        )

    def test_update_reader_book(self):
        self.maxDiff = None

        url = reverse('library_app:return', args=['1'])

        data = {
            "id": 1,
            "issue_date": "1987-03-12",
            "due_date": "1987-04-12",
            "book": 1,
            "reader": 1
        }

        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)

        data['due_date'] = '1987-05-12'

        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)
