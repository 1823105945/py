from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from .serializers import GoodsSerializer

class GoodsListView(APIView):
    '''商品列表'''
    def get(self,request,format=None):
        goods=Goods.objects.all()[:10]
        setializer=GoodsSerializer(goods,many=True)
        return Response(setializer.data)

