from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .pagination import CustomPagination
from .serializers import *
from rest_framework.generics import *
from .filters import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookFilterView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        print(genre)
        author = self.request.query_params.get('author')

        if genre is not None:
            queryset = queryset.filter(genre=genre)
        if author is not None:
            queryset = queryset.filter(authors=author)
        return queryset


class BookSearchView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title', 'authors']


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()
    pagination_class = CustomPagination


class ReaderCreateAPIView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all()


class ReaderFilterView(ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        queryset = Reader.objects.all()

        if self.request.user.is_authenticated:
            education = self.request.query_params.get('education')
            degree = self.request.query_params.get('degree')
            if degree is not None:
                queryset = queryset.filter(degree=degree)
            if education is not None:
                queryset = queryset.filter(education=education)
        return queryset


class ReaderDateOfBirthFilterView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReaderDateOfBirthFilter


class ReaderDateOfBirthRangeFilterView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReaderDateOfBirthRangeFilter


# class ReportApiView(ListAPIView):
#     serializer_class = ReportSerializer
#
#     books_by_hall = list(BookInHall.objects.annotate(books_by_hall=Sum('count')))
#     print(books_by_hall)
#     # books_total = sum([v['books_by_hall'] for v in books_by_hall])

# queryset = QuerySet([{'books_by_hall': books_by_hall}, {'books_total': books_total}])
# print(queryset)


class ReaderBookCreateAPIView(CreateAPIView):
    serializer_class = ReaderBookCreateSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # serializer_class = ReaderBookSerializer
    serializer_class = ReaderBookCreateSerializer
    queryset = ReaderBook.objects.all()

    # def destroy_list(self, request, *args, **kwargs):
    #     self.get_queryset().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderBookListAPIView(ListAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookAuthorView(ListAPIView):
    queryset = ReaderBook.objects.all()
    serializer_class = ReaderBookReaderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('book__title',)


class BookCoverCreateView(CreateAPIView):
    queryset = BookCover.objects.all()
    serializer_class = BookCoverSerializer


class BookCoverMultipleView(CreateAPIView):
    queryset = BookCover.objects.all()
    serializer_class = BookCoverSerializer

    def post(self, request, *args, **kwargs):
        print('post')

        files = request.FILES.getlist('file')
        print('got files', files)

        for f in files:
            print('f =', f.name)
            book_id = request.POST.get('book')
            file_instance = BookCover(book=Book.objects.get(id=book_id),
                                      file=f)
            file_instance.save()

        return Response(request.data, status=status.HTTP_201_CREATED)
