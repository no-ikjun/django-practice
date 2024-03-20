from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer