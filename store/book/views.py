from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializer

class BookListApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny,]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['author', 'publish_year', 'name']
    
