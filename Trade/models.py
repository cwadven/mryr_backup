# Create your models here.
from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Option(TimeStampedModel):
    options = models.CharField(max_length=100, unique=True, null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.options)


class TBoard(TimeStampedModel):
    """ 
    거래게시판 (꿀팁/사기관련 정보) 테이블
    """

    PAY_METHOD_CHOICES = (
        ('월세', '월세'),  # 월세
        ('년세', '년세'),  # 년세
        ('전세', '전세'),  # 전세
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #제목
    content = models.TextField() #내용 (상세설명)
    building = models.CharField(max_length=100)  # 건물명
    address = models.CharField(max_length=25) # 주소
    payment = models.CharField(
        max_length=100, choices=PAY_METHOD_CHOICES, default='월세')  # 월세 / 전세
    price = models.IntegerField() # 가격
    deposit = models.IntegerField() # 보증금
    area = models.FloatField() # 건물 면적 (평수)
    start_rent = models.DateField() #양도 시작 기간
    end_rent = models.DateField() #양도 마침 기간
    option = models.ManyToManyField(Option, blank=True)
    #사진 나중에

    # 좋아요 수
    @property
    def basket_count(self):
        return self.basket.all().count()

    def __str__(self):
        return self.building

class Basket(TimeStampedModel):
    """ 좋아요 테이블

    * To do
    1. creator -> User 외래키로 변경
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(TBoard, related_name='basket', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.author, self.post)


class Image(TimeStampedModel):
    post = models.ForeignKey(
        TBoard, related_name="images", on_delete=models.CASCADE)  # 1:N 관계
    images = models.ImageField(blank=True, null=True, upload_to='uploads/')

    def __str__(self):
        return '{} - {}'.format(self.post, self.images)