from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(RegisterSerializer): #RegisterSerializer를 상속받아서 수정하기 즉 오버라이팅 해서 Phone이라는 필드와 Credits라는 필드를 추가했음!
    Phone = serializers.CharField(
        required=False,
    )
    Credits = serializers.CharField(
        required=False,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['Phone'] = self.validated_data.get('Phone', '')
        data_dict['Credit'] = self.validated_data.get('Credit', '')
        return data_dict