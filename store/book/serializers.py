from rest_framework import serializers
from .models import Book


class BookSerializer(serializers):
    class Meta:
        model = Book
        fields = '__all__'