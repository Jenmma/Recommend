import pandas as pd
import numpy as np
from queue import Queue
def gettitle():
    train = pd.read_csv('../news.tsv', sep='\t')
    train = np.array(train)
    titles = train[:, 3]
    abstracts = train[:, 4]
    ids = train[:, 0]
    for i in range(len(titles)):
        titles[i] = int(len(titles[i].split()))
    for j in range(len(abstracts)):
        abstracts[j] = int(len(str(abstracts[j]).split()))
    # 标题长度1-57
    # 摘要长度1-474
    titcategory = np.zeros((6,))
    abscategory = np.zeros((10,))
    for index in range(len(titles)):
        titcategory[int(titles[index] / 10)] += 1.0
    for index in range(len(abstracts)):
        abscategory[int(abstracts[index] / 50)] += 1.0
    tit = {}
    tit["0-9"] = titcategory[0]
    tit["10-19"] = titcategory[1]
    tit["20-29"] = titcategory[2]
    tit["30-39"] = titcategory[3]
    tit["40-49"] = titcategory[4]
    tit["50-59"] = titcategory[5]
    x=["0-9","10-19","20-29","30-39","40-49","50-59"]
    y=[]
    for i in range(0,6):
        y.append(titcategory[i])
    print(x,y)
    abst = {}
    abst["0-49"] = abscategory[0]
    abst["50-99"] = abscategory[1]
    abst["100-149"] = abscategory[2]
    abst["150-199"] = abscategory[3]
    abst["200-249"] = abscategory[4]
    abst["250-299"] = abscategory[5]
    abst["300-349"] = abscategory[6]
    abst["350-399"] = abscategory[7]
    abst["400-449"] = abscategory[8]
    abst["450-499"] = abscategory[9]
    temp=[]
    for i in abst:
        temp1={'value',abst[i]}
        temp2={'name',i}
        temp.append({'name':i,'value':abst[i]})
    print(temp)
    result={}
    result["datax"]=x
    result["datay"]=y
    result["abstdata"]=temp
    return result



gettitle()

