# 该文件用来对库中数据增删查改操作

from app.models import User, UserRelation
from queue import Queue
import pandas as pd


# 获取所有子节点id的处理函数
def getnodes(userid):
    nodes = []
    qe = Queue(maxsize=20)
    qe.put(int(userid))
    while(qe.empty() == False):
        id = qe.get()
        nodes.append(id)
        temp = getuseridonelevel(id)
        if(temp['empty'] != 1):
            for item in temp['nodes']:
                qe.put(item)
    nodes = pd.unique(nodes).tolist()
    return nodes


# 依据id获取所有节点信息
# 数据格式
# {
#     "id": "0",
#     "name": "Myriel",
#     "symbolSize": 19.12381,//页面节点相对大小
#     "value": 28.685715,
#     "category": 0//种类
# }
def getnodesdetail(userid):
    response = {'data': [], 'ok': 0, 'msg': ''}
    nodes = []
    nodes = getnodes(userid)
    for node in nodes:
        obj = {}
        detail = User.objects.get(id=node)
        obj["id"] = str(detail.id)
        obj["name"] = detail.name
        obj['symbolSize'] = detail.value
        obj['value'] = detail.value
        obj['category'] = str(detail.categoryName)
        response['data'].append(obj)
    response['ok'] = 1
    return response

# 获取所有子节点之间的联系
# 数据格式
# {
#     "source": "62",//两节点之间的连线
#     "target": "59"
# },


def getlinks(userid):
    response = {'data': [], 'ok': 0, 'msg': ''}
    qe = Queue(maxsize=20)
    qe.put(int(userid))
    while(qe.empty() == False):
        id = qe.get()
        temp = getuseridonelevel(id)
        if(temp['empty'] != 1):
            for relation in temp['relations']:
                link = {'source': "", "target": ""}
                link['source'] = str(relation['startid'])
                link['target'] = str(relation['endid'])
                response['data'].append(link)
            for item in temp['nodes']:
                qe.put(item)
    response['ok'] = 1
    return response

# 获取下一层的子节点


def getuseridonelevel(userid):
    result = {'nodes': [], 'relations': [], 'empty': 1}
    relas = []
    nodes = []
    relations = UserRelation.objects.filter(startid=userid)
    if(relations.exists()):
        result['empty'] = 0
        for relation in relations:
            nodes.append(relation.endid)
            obj = {}
            obj['startid'] = relation.startid
            obj['endid'] = relation.endid
            relas.append(obj)

    result['nodes'] = nodes
    result['relations'] = relas
    return result

# 获取子节点所涉及的类目属性
# 数据格式
# {
#     "name": "类目8"
# }


def getcategories(userid):
    response = {'data': [], 'ok': 0, 'msg': ''}
    nodes = []
    nodes = getnodes(userid)
    categories = []
    for node in nodes:
        categories.append(User.objects.get(id=node).categoryName)

    categories = pd.unique(categories).tolist()
    for category in categories:
        obj = {}
        obj['name'] = category
        response['data'].append(obj)
    response['ok'] = 1
    return response
