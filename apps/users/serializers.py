
from  rest_framework import serializers
from MxShop.settings import REGEX_MOBILE
import re
from datetime import datetime
from datetime import timedelta
from .models import VerifyCode,UserProfile
from rest_framework.validators import UniqueValidator


class SmsSerializer(serializers.Serializer):
    mobile=serializers.CharField(max_length=11)

    def validate_mobile(self,mobile):
        '''验证手机号码'''

        # 验证法频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count:
            return serializers.ValidationError("用户已经存在")
#         验证手机号码是否合法
        elif not re.match(REGEX_MOBILE,mobile):
            return serializers.ValidationError("手机号码不正确")
        elif VerifyCode.objects.filter(add_time_gt=one_mintes_ago,mobile=mobile).count():
            return serializers.ValidationError("距离上次发送未超过60秒")
        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code =serializers.CharField(required=True,max_length=4,min_length=4,help_text="验证码",label="验证码",write_only=True,error_messages={
        "blank":"请输入验证码",
        "required":"请输入验证码",
        "max_length":"验证码格式错误",
        "min_length":"验证码格式错误",
    })
    username=serializers.CharField(label="用户名",required=True,allow_blank=False,validators=[UniqueValidator(queryset=UserProfile.objects.all(),message="用户已存在")])
    password=serializers.CharField(
        style={'input_type':'password'},label="密码",write_only=True,
    )

    def create(self, validated_data):
        user=super(UserRegSerializer,self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self,code):
        verify_records=VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by()
        if verify_records:
            last_record=verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago>last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            elif last_record !=code:
                raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"]=attrs["username"]
        del attrs["code"]
        return attrs


    class Meta:
        model=UserProfile
        fields=("username","code","mobels","password")