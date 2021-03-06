from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Goods
# from .serializers import GoodsSerializer
# 方式1
# class GoodsListView(APIView):
#     '''商品列表'''
#     def get(self,request,format=None):
#         goods=Goods.objects.all()[:10]
#         setializer=GoodsSerializer(goods,many=True)
#         return Response(setializer.data)


# 方式2
# 分页方式1
# from rest_framework import generics
# from .models import Goods
# from .serializers import GoodsSerializer
# class GoodsListView(generics.ListAPIView):
#     '''商品列表'''
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# 分页方式2
# 自定义每页大小
# from rest_framework import generics
# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework.pagination import PageNumberPagination
#
# class GoodsPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     page_query_param = "p"
#     max_page_size = 100
#
#
# class GoodsListView(generics.ListAPIView):
#     '''商品列表'''
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination




# 方式3
from .models import Goods,GoodGategory
from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


class GoodsListView(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''商品列表 ,分页，搜索，过滤，排序'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend ,filters.SearchFilter,filters.OrderingFilter)
    # filter_filelds=('name','shop_price')
    filter_filelds =GoodsFilter()
    search_fields=('name','goods_brief','goods_desc')
    ordering_fields=('sold_num','shop_price')

    # # 做过滤
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min=self.request.query_params.get("price_min",0)
    #     if price_min:
    #         queryset=queryset.filter(shop_price=int(price_min))
    #     return queryset



class CategoryVuewset(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    '''
    list:
    商品分类列表数据
    '''
    queryset = GoodGategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer






