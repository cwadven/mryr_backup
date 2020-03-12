from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.

class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class Board_CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class Board_LikessViewset(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer