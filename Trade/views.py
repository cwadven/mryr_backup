from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# Create your views here.
from rest_framework.response import Response
from rest_framework import status

class TBoardViewset(viewsets.ModelViewSet):
    queryset = TBoard.objects.all()
    serializer_class = TBoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,) #로그인된 사람은 쓸 수 있고 대신, 자기만의 것은 자기만 수정 가능  --> permissions.py 에서 class 만들어서 적용

    def perform_create(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)

    def perform_update(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        serializer.save(author=self.request.user)

class BasketViewset(viewsets.ModelViewSet): ########get 할때 특정 사람과 특정 게시판만 필터링 되도록 추후에 추가
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,) #로그인된 사람은 쓸 수 있고 대신, 자기만의 것은 자기만 수정 가능  --> permissions.py 에서 class 만들어서 적용

    def get_queryset(self):
        qs = super().get_queryset()
        try:
            qs = qs.filter(author=self.request.user)
            if qs:
                return qs
            else:
                return None
        except:
            return None

    def perform_create(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user, post=serializer.validated_data["post"]) #해당 게시판에 있을 경우 serializer.validated_data를 통해서 가져온 속성을 체크할 수 있다
        if qs:
            #print("있어!!") #추가적인 like를 못하게 설정
            return Response(status=status.HTTP_404_NOT_FOUND) #추후에 에러 추가 필요 !!!!!!!!!!!!!!!
        else:
            serializer.save(author=self.request.user)

    def perform_update(self, serializer): #자동으로 자기 자신 author에 저장 되도록
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user, post=serializer.validated_data["post"]) #해당 게시판에 있을 경우 serializer.validated_data를 통해서 가져온 속성을 체크할 수 있다
        if qs:
            #print("있어!!") #추가적인 like를 못하게 설정
            return Response(status=status.HTTP_404_NOT_FOUND) #추후에 에러 추가 필요 !!!!!!!!!!!!!!!
        else:
            serializer.save(author=self.request.user)