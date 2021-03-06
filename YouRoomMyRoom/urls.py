"""YouRoomMyRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import Board.urls
import Trade.urls
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

schema_view = get_schema_view(
    openapi.Info(
        title="니방내방",
        default_version='verson 0.1.0',
        description="자취방 양도 서비스 플랫폼",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Trade.urls')),
    path('board/', include('Board.urls')),
    path('api-auth/', include('rest_framework.urls')),

    #로그인 및 회원가입
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- 일단 자동으로 토큰 생성을 만들지 못해서 임시로 만듦


    # Auto DRF API docs
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
]
