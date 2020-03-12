from .models import *
from rest_framework import serializers

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Likes
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer): #JSON으로 주는 녀석, Post를 하는 form 같은 녀석
    comments = CommentsSerializer(many=True, required=False, read_only=True) #관계가 있는 녀석 보여주기 required = False로 해야 추가 안해도 Post가 되도록
    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'content', #comments로 가져온 fields도 추가가 가능하다
                  'comments', 'likes_count', 'comments_count') #likes_count 랑 comments_count는 model에서 property로 가져온 녀석이다