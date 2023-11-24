from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Book
from .serializers import BookSerializer

class BookListApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

