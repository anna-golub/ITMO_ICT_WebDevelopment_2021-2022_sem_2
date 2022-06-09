from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import *


class BookCreateTest(TestCase):

    def test_create_book(self):
        url = reverse('library_app:books_create')

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

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


# class ReaderCreateTest(TestCase):
#
#     def test_create_reader(self):
#         self.maxDiff = None
#         url = reverse('library_app:readers_create')
#
#         data_request = {
#             'username': 'linaanil',
#             'password': 'linaani19908911',
#             'email': 'lina@gmail.com',
#             'card_number': 111,
#             'first_name': 'Lina',
#             'last_name': 'Anil',
#             'passport': '1111111111',
#             'date_of_birth': '1990-09-09',
#             'address': '...',
#             'phone': '89111111111',
#             'education': 'Среднее общее',
#             'degree': False
#         }
#
#         data_response_exp = {
#             'id': 1,
#             'last_login': None,
#             'is_superuser': False,
#             'email': '',
#             'is_staff': False,
#             'is_active': True,
#             # 'date_joined': '',
#             'username': '',
#             'password': '',
#             'card_number': 111,
#             'card_number_old': None,
#             'first_name': 'Lina',
#             'last_name': 'Anil',
#             'passport': '1111111111',
#             'date_of_birth': '1990-09-09',
#             'address': '...',
#             'phone': '89111111111',
#             'education': 'Среднее общее',
#             'degree': False,
#             'reader_hall': None,
#             'groups': [],
#             'user_permissions': [],
#             'reader_book': []
#         }
#
#         response = self.client.post(url, data_request, format='json')
#         print(response.json())
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         data_response_act = {k: v for k, v in response.data.items() if k not in ('date_joined', 'password')}
#
#         self.assertEqual(data_response_act, data_response_exp)


class ReaderBookCreateTest(TestCase):
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

    def test_create_reader_book(self):
        self.maxDiff = None

        url = reverse('library_app:take_out')

        data = {
            "id": 1,
            "issue_date": "1987-03-12",
            "due_date": "1987-04-12",
            "book": 1,
            "reader": 1
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
