from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SmsSerializer,UserRegSerializer
from random import choice
from .models import VerifyCode,UserProfile


User=settings.AUTH_USER_MODEL

class CustomBackend(ModelBackend):
    # 自定义用户验证
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''f发送短信验证码'''
    serializer_class = SmsSerializer

    def generate_code(self):
        '''利用随机数生成四位数字的验证码'''
        seeds = '1234567890'
        random_str=[]
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile=serializer.validated_data['mobile']
        code=self.generate_code()
        code_record = VerifyCode(code=code,mobile=mobile)
        code_record.save()

class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''用户'''
    serializer_class = UserRegSerializer
    queryset = UserProfile.objects.all()

