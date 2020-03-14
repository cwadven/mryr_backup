from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import DefaultRouter # class 를 경로 지정하기 위해서

from . import views

router = DefaultRouter() #view에 있는 함수(클래스를 가져오기 위해서는 router 사용)
# router.register('Board', views.BoardViewset)
# router.register('Board_Comments', views.Board_CommentsViewset)
# router.register('Board_Likes', views.Board_LikessViewset)

urlpatterns = [
    #path('', include(router.urls)),
]