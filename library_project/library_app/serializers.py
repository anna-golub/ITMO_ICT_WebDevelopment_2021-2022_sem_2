from rest_framework import serializers
from .models import *
from .validators import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"

    def create(self, validated_data):
        user = Reader(
            email=validated_data['email'],
            username=validated_data['username']
            # TODO: добавить остальные параметры, чтобы они сохранялись
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BookRetrieveSerializer(serializers.ModelSerializer):
    book_hall = HallSerializer(many=True)
    book_reader = ReaderSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class ReaderRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    reader_book = BookSerializer(many=True)

    class Meta:
        model = Reader
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class ReaderBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = "__all__"


class ReaderBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    reader = ReaderSerializer()

    class Meta:
        model = ReaderBook
        fields = "__all__"


class ReaderBookReaderSerializer(serializers.ModelSerializer):
    reader = ReaderSerializer()

    class Meta:
        model = ReaderBook
        fields = "__all__"


class BookCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCover
        fields = ['book', 'file']
