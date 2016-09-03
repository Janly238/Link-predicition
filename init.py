# -*- coding: utf-8 -*-
from numpy import *

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    originalMat = zeros((numberOfLines,2))
    index =0
    for line in arrayOLines:
            line = line.strip()
            listFromLine =line.split('    ')
            originalMat[index,:]=(int(listFromLine[0]),int(listFromLine[1]))
            index +=1
            
    maxnum=int(amax(originalMat))
    addMat = zeros((numberOfLines+maxnum,2))
    addMat[0:numberOfLines,:]=originalMat[0:numberOfLines,:]
    index=1
    for i in range(numberOfLines,numberOfLines+maxnum):
            addMat[i,:]=(index,index)
            index+=1
    return maxnum,originalMat,addMat,numberOfLines
    
def divideSet(originalMat,lableMat,trainProportion,LinesLength):
    order=arange(0,LinesLength,1)
    random.shuffle(order)
    EtLable=zeros((int(LinesLength*trainProportion),2))
    EpLable=zeros((int(LinesLength*(1-trainProportion))+1,2))
    for i in range(0,int(LinesLength*trainProportion)):
            EtLable[i,:]=originalMat[order[i],:]
            u,v=originalMat[order[i],:]
            lableMat[v,u]=lableMat[u,v]=1
            
    index=0
    for i in range(int(LinesLength*trainProportion),LinesLength):
            EpLable[index,:]=originalMat[order[i],:]
            u,v=originalMat[order[i],:]
            lableMat[v,u]=lableMat[u,v]=2
            index +=1
    return EtLable,EpLable,lableMat
    
    