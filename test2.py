# -*- coding: utf-8 -*-
import similarity2 
import init
import networkx as nx
import matplotlib.pyplot as plt
from numpy import *
import operator
import plotRoc
import auc

maxnum,originalMat,addMat,Lineslength=init.file2matrix('USAir.txt')

G=nx.Graph()
allnotes=arange(1,maxnum+1,1)
G.add_nodes_from(allnotes)
testlable=zeros((Lineslength,13))   #存在边的测试lable
lableMat = zeros((maxnum+1,maxnum+1))   #矩阵，连边为1，没连边为0
testlable[0:Lineslength,0:2]=originalMat[0:Lineslength,:]
finalLable=zeros((maxnum*(maxnum-1)/2,13))
ULable=zeros((maxnum*(maxnum-1)/2,2))
MLable=zeros((len(ULable)-Lineslength,2))  #+1?
        
trainProportion=0.9
EtLable,EpLable,lableMat=init.divideSet(originalMat,lableMat,trainProportion,Lineslength)       
G.add_edges_from(EtLable)

index=0
for i in range(1,maxnum+1):
		j=i+1
		while(j<maxnum+1):
                  finalLable[index,0:2]=(i,j)
                  ULable[index,0:2]=(i,j)
                  finalLable[index,12]=lableMat[i,j]
#==============================================================================
#                   if(len(list(nx.common_neighbors(G, i, j)))==0):
#                           finalLable[index,12]=0
#==============================================================================
                  j+=1
                  index+=1
                  
print 'finished init' 

#==============================================================================
# testarray=similarity2.CommonNeighbors(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,2]=i
#         index+=1
# print 'finished 1st'
# 
# testarray=similarity2.Salton(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,3]=i
#         index+=1
# print 'finished 2nd'
# 
# testarray=similarity2.Jaccard(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,4]=i
#         index+=1
# print 'finished 3rd'
# 
# testarray=similarity2.Sorenson(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,5]=i
#         index+=1
# print 'finished 4th'
# 
# testarray=similarity2.HubPromoted(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,6]=i
#         index+=1
# print 'finished 5th'
# 
# testarray=similarity2.HubDepressed(G,ULable)
# index=0 
# for i in testarray:
#         finalLable[index,7]=i
#         index+=1
# print 'finished 6th'
# 
# testarray=similarity2.Leicht_Holme_Newman(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,8]=i
#         index+=1
# print 'finished 7th'
# 
# testarray=similarity2.Preferential_attachment(G,ULable)
# index=0
# for i in testarray:
#         finalLable[index,9]=i
#         index+=1
# print 'finished 8th'
#==============================================================================
#==============================================================================
# 
# testarray=similarity.Adamic_Adar(G,originalMat)
# index=0
# for i in testarray:
#         testlable[index,10]=i
#         index+=1
# print 'finished 9th'
# 
# testarray=similarity.Resource_Allocation(G,originalMat)
# index=0
# for i in testarray:
#         testlable[index,11]=i
#         index+=1
# print 'finished 10th'
#==============================================================================

preds=nx.jaccard_coefficient(G,ULable)
index=0
for u,v,p in preds:
        finalLable[index,8]=p
        index+=1
print 'finished 7th' 

#==============================================================================
# preds=nx.jaccard_coefficient(G,originalMat)
# index=0
# for u,v,p in preds:
#         testlable[index,2]=p
#         index+=1
# print 'finished 7th' 
#==============================================================================

preds=nx.preferential_attachment(G,ULable)
index=0
for u,v,p in preds:
        finalLable[index,9]=p
        index+=1
print 'finished 8th' 

preds=nx.adamic_adar_index(G,ULable)
index=0
for u,v,p in preds:
        finalLable[index,10]=p
        index+=1
print 'finished 9th' 

preds=nx.resource_allocation_index(G,ULable)
index=0
for u,v,p in preds:
        finalLable[index,11]=p
        index+=1
print 'finished 10th' 

ddd=auc.auc2(finalLable)

#nx.draw(G)
#plt.show(G)