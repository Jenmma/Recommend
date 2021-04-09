from django.shortcuts import render
from django.http import JsonResponse
from app.service import user
from django.core import serializers
from django.views.decorators.http import require_http_methods

# Create your views here.
# 和路由对应的数据打包函数


@require_http_methods(["GET"])
def getrelationchart(request):
    response = {}
    try:
        userid = request.GET.get('userid')
        obj = {}

        obj["nodes"] = user.getnodesdetail(userid)["data"]
        obj["links"] = user.getlinks(userid)["data"]
        obj["categories"] = user.getcategories(userid)["data"]
        response["data"] = obj
        response["ok"] = 1
        
    except Exception as e:
        response['msg'] = str(e)
        response['ok'] = 0
    return JsonResponse(response)
