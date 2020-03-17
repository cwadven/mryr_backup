from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class TBoardViewset(viewsets.ModelViewSet):
    queryset = TBoard.objects.all()
    serializer_class = TBoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,) #로그인된 사람은 쓸 수 있고 대신, 자기만의 것은 자기만 수정 가능  --> permissions.py 에서 class 만들어서 적용

    def perform_create(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)

    def perform_update(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)

class BasketViewset(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,) #로그인된 사람은 쓸 수 있고 대신, 자기만의 것은 자기만 수정 가능  --> permissions.py 에서 class 만들어서 적용

    def perform_create(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)

    def perform_update(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)