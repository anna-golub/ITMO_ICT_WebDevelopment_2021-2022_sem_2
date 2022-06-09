from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import *

import datetime


class BookRetrieveTest(TestCase):
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

    def test_retrieve_book(self):
        url = reverse('library_app:books_retrieve', args=['1'])

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

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class ReaderRetrieveTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_retrieve_reader(self):
        self.maxDiff = None

        url = reverse('library_app:readers_retrieve', args=['1'])
        today = str(datetime.date.today())

        data = {
            'id': 1,
            'last_login': None,
            'is_superuser': False,
            'email': '',
            'is_staff': False,
            'is_active': True,
            'date_joined': today,
            'username': '',
            'password': '',
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

        request_data = {k: v for k, v in data.items() if v is not None}
        response = self.client.get(url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        response_data['date_joined'] = response_data['date_joined'][:10]
        self.assertEqual(response_data, data)


class BookFilterSearchTest(TestCase):
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

    def test_search_book(self):
        self.maxDiff = None
        url = reverse('library_app:books_search')

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {'id': 1,
                 'title': 'Аэлита',
                 'authors': 'А. Толстой',
                 'publisher': 'Русская литература',
                 'publication_year': 1956,
                 'genre': 'Фантастика',
                 'book_cypher': '97',
                 'book_hall': [],
                 'book_reader': []
                 }
            ]
        }

        response = self.client.get(url, {'search': 'то'}, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
