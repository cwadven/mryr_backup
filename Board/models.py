from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(TimeStampedModel):
    """ 자유게시판 (꿀팁/사기관련 정보) 테이블

    * To do
    1. author -> User 외래키로 변경
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()

    # 좋아요 수
    @property
    def likes_count(self):
        return self.likes.all().count()

    # 댓글 수
    @property
    def comments_count(self):
        return self.comments.all().count()

    def __str__(self):
        return self.title


class Comments(TimeStampedModel):
    """ 게시판 관련 댓글 테이블 

    * To do
    1. creator -> User 외래키로 변경
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey(
        Board, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.author, self.message)


class Likes(TimeStampedModel):
    """ 좋아요 테이블

    * To do
    1. creator -> User 외래키로 변경
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Board, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.author, self.post)
