
from django.views.generic.base import View
from goods.models import Goods
import json
from django.core import serializers

class GoodsListView(View):
    def get(self,request):
        goods=Goods.objects.all()[:10]
        json_list=[]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"]=good.name
        #     json_dict["category"]=good.category
        #     json_dict["market_price"]=good.market_price
        #     json_list.append(json_dict)


        json_data=serializers.serialize("json",goods)
        json_data=json.loads(json_data)
        from  django.http import HttpResponse,JsonResponse
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(json_data,safe=False)