"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

# import xadmin
from MxShop.settings import  MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListView,CategoryVuewset
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset,UserViewset
from rest_framework.documentation import include_docs_urls
# urlpatterns = [
#     # path(r'^xadmin/', xadmin.site.urls),
#     url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
#     url(r'goods/$',GoodsListView.as_view(),name="goods-list"),
#     # url(r'^docs/$', include_docs_urls(title="慕学生鲜")),
#     url(r'^api-auth/', include('rest_framework.urls'))
# ]
# 方式3配套
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
# 配置url
router.register(r'goods',GoodsListView,base_name='goods')
router.register(r'categorys',CategoryVuewset,base_name='categorys')
router.register(r'codes',SmsCodeViewset,base_name='codes')
router.register(r'users',UserViewset,base_name='users')

goods_list = GoodsListView.as_view({
    'get': 'list',
})

urlpatterns = [
    # path(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    #drf自带的token认证模式
    url(r'^api-token-auth/',views.obtain_auth_token),
    #jwt的认证接口
    # 登录
    url(r'^login/',obtain_jwt_token),
]


