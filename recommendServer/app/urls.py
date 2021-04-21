# 处理函数和后端路由之间的映射关系

from django.conf.urls import url
from app import views

urlpatterns = [
    # 路由映射关系
    url(r'relationchart$', views.getrelationchart, ),
    url(r'test$',views.length,),
]
