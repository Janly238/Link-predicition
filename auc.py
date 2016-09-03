# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:01:18 2016

@author: jj
"""
from numpy import *
def auc2(finalLable):
    aucScore=[]
    for i in range(8,12):
        sortOrder=argsort(finalLable[:,i],axis=0)
        for j in range(0,len(sortOrder)):
            finalLable[sortOrder[j],7]=j
        aaa=finalLable[argwhere(finalLable[:,12]==2),7] #Tp排名
        bbb=finalLable[argwhere(finalLable[:,12]==0),7] #M排名
        sum=0
        for x in aaa:
            for y in bbb:
                if(x>y):
                    sum+=1
        ccc=sum/float(len(aaa)*len(bbb))
        aucScore.append(ccc)
    return aucScore