from .models import *
from rest_framework import serializers
#from Account.serializer import UserSerializer # 성민이 형은 User App
from Account.models import Profile # 성민이 형은 User App

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'post', 'images')

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'options')

class UserSerializer(serializers.ModelSerializer): #author 안에 있는 정보를 가져오기 위해서 TBoard랑 author로 관계가 있는 UserSerializer를 통해서 새로 만듦  
    class Meta:
        model = Profile
        fields = ("id", "username", "Credit", "Phone", )     

class BasketSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴
    
    class Meta:
        model = Basket
        fields = ('id', 'author_name', 'post',)

class TBoardSerializer(serializers.ModelSerializer): #JSON으로 주는 녀석, Post를 하는 form 같은 녀석
    author = UserSerializer(read_only=True)
    #author_name = serializers.ReadOnlyField(source='author.username') #모델 author를 참조하는 곳에있는 user name을 가져옴
    option_name = serializers.SerializerMethodField() #함수를 통해서 새로운 필드 값을 return 하고 싶을 경우 SerializerMethodField()를 이용
    basket_confirm = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)
    #ImageSerializer(many=True, read_only=True) 할 경우 many랑 꼭 확인하자.... (many를 적지 않을 경우 안보일 경우가 있다)
    #관계로 묶여진 필드의 자세한 정보를 알고 싶을 경우 새로운 Serializer를 생성한후 해당 모델을 적용 그 후, 관계로 묶여져있는 해당 필드의 이름으로 Serializer를 묶는다

    class Meta:
        model = TBoard
        fields = ('id', 'author', 'title', 'content', 'building', #comments로 가져온 fields도 추가가 가능하다
                  'address', 'payment', 'price', 'deposit', 'area', 'option', 'option_name', 'start_rent', 'end_rent', 'images', 'basket_confirm', ) #likes_count 랑 comments_count는 model에서 property로 가져온 녀석이다
        extra_kwargs = {
            'option': {'write_only': True, } # 값을 반환해 줄 경우 사용자에게는 안보이도록 설정
        }
        #read_only_fields = ('author', )
        #option을 따로 설정 해야된다!
        #option 은 옵션 설정하는 필드 ==> POST를 할 때는 해당 option 필드에 값을 넣어야 한다!
        #option_name 은 옵션 설정하는 필드가 반환될 때, id 값으로 나와서! 해당 id를 참조해 옵션의 이름을 사용자에게 보여주기 위한 필드 (예 : 화장실, 배란다 등)

    def get_basket_confirm(self, obj): #좋아요를 했는지 안했는지 판별
        try:
            find_basket = Basket.objects.filter(author=self.context.get('request').user, post=obj.id) #get하면 오류 나와서
        except:
            find_basket = False #사용자가 없을 경우

        if find_basket:
            return "True"
        else:
            return "False"

    def get_option_name(self, obj): #직업 하나의 필드를 만들어서 ManytoMany의 녀석안에 있는 정보를 가져와서 담음
        options_list = []
        options_get = obj.option.all()
        for a in options_get:
            options_list.append(a.options)
        return options_list


    