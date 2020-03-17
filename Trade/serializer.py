from .models import *
from rest_framework import serializers

class BasketSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴

    class Meta:
        model = Basket
        fields = ('id', 'author_name', 'post',)

class TBoardSerializer(serializers.ModelSerializer): #JSON으로 주는 녀석, Post를 하는 form 같은 녀석
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴
    
    class Meta:
        model = TBoard
        fields = ('id', 'author_name', 'title', 'content', 'address', 'payment', 'area', 'start_rent', 'end_rent',) #comments로 가져온 fields도 추가가 가능하다 #likes_count 랑 comments_count는 model에서 property로 가져온 녀석이다
        #이 필드는 꼭 required일 필요는 없다! 라는 것을 쓰면됨