from django.shortcuts import render
from django.http import JsonResponse
from app.service import user
from django.core import serializers
from django.views.decorators.http import require_http_methods
from app.service import test_mind

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


@require_http_methods(["GET"])
def length(request):
    response = {}
    try:
        '''返回值类型
        data:
        {
           title:
           {
              data:
                {
                   datax:[]//x坐标
                   datay:[]//y坐标
                }
                title:""//此图的标题
                shuxing:""//值的属性（数量，销量）
           }
           abstract:
           {
              title:
              dataname:['','','']//所有数据的名字，放在饼状图底部显示
              abstdata:
              [
                 {value:,name:}
                 {value:,name:}
              ]
           }
        }
        '''
        temp=test_mind.gettitle()
        title={}
        title["data"]={"datax":temp["datax"],"datay":temp["datay"]}
        title["title"]="标题长度分布"
        title["property"]="数量"
        abstract={}
        abstract["title"]="简介长度分布"
        abstract["dataname"]=[i["name"] for i in temp["abstdata"]]
        abstract["abstdata"]=temp["abstdata"]
        response["data"]={"title":title,"abstract":abstract}
        response["ok"]= 1
    except Exception as e:
        response['msg'] = str(e)
        response['ok'] = 0
    return JsonResponse(response)