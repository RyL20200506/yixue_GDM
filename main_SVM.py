# -*- coding: utf-8 -*-
'''
#这个代码要完成对数据的读取和清洗，删除空白数据，以及利用svm算法进行简单预测
Data:10.13
Auther:Zherui.Liu
'''
import readexcel
reload(readexcel)
import svmMLiA
from sklearn.decomposition import PCA
import sklearn
import numpy as np
import ForX
reload(ForX)

forx = [0,1,2,3,4,5]
xls = 'GDM'#这个就表示是使用1之后的葡萄糖血量作为自变量。
xlsname = xls + '.xls' #这里填写待处理的数据，需要加上后缀
alldata = readexcel.readxls(xlsname) #读取数据先
clcdata = readexcel.clc(alldata) #清洗数据
ForX.list2cav('clcdata.csv',clcdata)
X,Y = readexcel.list2XY(clcdata,forx) #选取哪些作为自变量
X =  ForX.gui1hua_yi(X)
X1 = X[0:2000]
Y1 = Y[0:2000]
X2 = X[2000:2974]
Y2 = Y[2000:2974]
#readexcel.write(clcdata) #将清洗过的数据重新写成txt
#pre1,sVs,labelSV,alphas,svInd,b= svmMLiA.Justraining(1.2,X1,Y1)
pre1,pre2= svmMLiA.training(1.2,X1,Y1,X2,Y2)
ForX.list2cav(xls + 'pre1.csv',pre1)
ForX.list2cav(xls + 'pre2.csv',pre2)
ratiofhave = ForX.RatiofHave(pre2) #判断有病的准确率
ratiofzero = ForX.RatiofZero(pre2)
print "判断有的失误率："+str(ratiofhave)+',判断无的失误率：'+str(ratiofzero)
