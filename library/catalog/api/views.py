from rest_framework import viewsets
from rest_framework.response import Response
from catalog.models import Author,Book
from .serializers import AuthorSerializers,BookSerializers

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    