from rest_framework import serializers
from .models import *
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class ProfileSerializer(RegisterSerializer): #RegisterSerializer를 상속받아서 수정하기 즉 오버라이팅 해서 Phone이라는 필드와 Credits라는 필드를 추가했음!
    Phone = serializers.CharField(
        required=False,
        max_length=13,
    )
    Credit = serializers.FloatField(
        required=False,
    )

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         Token.objects.create(user=instance)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['Phone'] = self.validated_data.get('Phone', '')
        data_dict['Credit'] = self.validated_data.get('Credit', 0)
        return data_dict

        