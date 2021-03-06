from .models import *
from rest_framework import serializers

class CommentsSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴
    
    class Meta:
        model = Comments
        fields = ('id', 'author_name', 'post', 'message',)

class LikesSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴

    class Meta:
        model =Likes
        fields = ('id', 'author_name', 'post',)

class BoardSerializer(serializers.ModelSerializer): #JSON으로 주는 녀석, Post를 하는 form 같은 녀석
    comments = CommentsSerializer(many=True, required=False, read_only=True) #관계가 있는 녀석 보여주기 required = False로 해야 추가 안해도 Post가 되도록
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴
    likes_confirm = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'author_name', 'title', 'content', #comments로 가져온 fields도 추가가 가능하다
                  'comments', 'likes_count', 'comments_count', 'likes_confirm',) #likes_count 랑 comments_count는 model에서 property로 가져온 녀석이다
        #read_only_fields = ('author', )

    def get_likes_confirm(self, obj): #좋아요를 했는지 안했는지 판별
        try:
            a = Likes.objects.filter(author=self.context.get('request').user, post=obj.id) #get하면 오류 나와서
        except:
            a = False #사용자가 없을 경우

        if a:
            return "True"
        else:
            return "False"