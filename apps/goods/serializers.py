

from rest_framework import serializers
from goods.models import Goods,GoodGategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodGategory
        # fields=("name","click_num","market_price","add_time")
        fields="__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Goods
        # fields=("name","click_num","market_price","add_time")
        fields="__all__"

