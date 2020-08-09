# -*- coding:utf-8 -*-
#这个当然就是想要用来测试boosting的机器学习效果了
#Author:刘哲瑞 17-11-2

from sklearn.ensemble import GradientBoostingClassifier
import svmMLiA
import functions
reload(functions)
import readexcel
import ForX
reload(ForX)

forx = [0,1,2,3,4]
xls = 'GDM1'#这个就表示是使用1之后的葡萄糖血量作为自变量。
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
clf = GradientBoostingClassifier(n_estimators=10)
clf = clf.fit(X1,Y1)
preY1 = clf.predict(X1)
preY2 = clf.predict(X2)
preY1 = preY1.tolist()
preY2 = preY2.tolist()

errMat0,errnumrate0,whichlist0 = functions.forerr(Y1,preY1)
errMat1,errnumrate1,whichlist1 = functions.forerr(Y2,preY2)
auc = functions.AUC(Y2,preY2)

ForX.list2cav(xls + 'pre1.csv',whichlist0)
ForX.list2cav(xls + 'pre2.csv',whichlist1)
a11=errMat1[0]
a12=errMat1[1]
a21=errMat1[2]
a22=errMat1[3]
mingandu,teyidu,posidu,negdu=functions.forate(errMat1)
print 'rirate:'+str((a11+a22)/float(a11+a12+a21+a22))
print  '敏感'+str(mingandu),'特异'+str(teyidu),'posidu'+str(posidu),'negdu'+str(negdu)
print 'AUC'+str(auc)