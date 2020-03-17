# Create your models here.
from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TBoard(TimeStampedModel):
    """ 
    거래게시판 (꿀팁/사기관련 정보) 테이블
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    address = models.CharField(max_length=25)
    payment = models.BooleanField()
    area = models.FloatField()
    start_rent = models.DateField()
    end_rent = models.DateField()
    #사진 나중에

    # 좋아요 수
    @property
    def basket_count(self):
        return self.basket.all().count()

    def __str__(self):
        return self.title

class Basket(TimeStampedModel):
    """ 좋아요 테이블

    * To do
    1. creator -> User 외래키로 변경
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(TBoard, related_name='basket', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.author, self.post)
