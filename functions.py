# -*- coding:utf-8 -*-
#用来存放一些简单的，常用的函数
#Author：刘哲瑞

def forerr(Y,preY):#一看就是想要比较Y和preY的差距吧,要求他们都是list
    errnum = 0
    righterr = 0 #判1但是错
    rightnum = 0 #判断1的次数
    worerr = 0 #判0但是错
    wornum =0 #判断0的次数
    whichlist = []
    a11=0 #判断有病且判断正确
    a12=0
    a21=0
    a22=0 #判断没病且判断正确
    if len(Y)!=len(preY):
        print 'the length of each Y is different,are u fucking kidding me?'
    for i in range(len(Y)):
        if Y[i]==1 and preY[i]==1:
            a11 = a11+1
        else:
            if Y[i]==1 and preY[i]!=1:
                a12 = a12+1
            elif Y[i]!=1 and preY[i]==1:
                a21=a21+1
            elif Y[i]!=1 and preY[i]!=1:
                a22=a22+1
    #可以使用a11+a12的值结合excel来验算代码是否有错
    for i in range(len(Y)):
        print Y[i],preY[i]
        if Y[i]!=preY[i]:
            print 'wor'
            if preY[i]==1:
                righterr = righterr + 1
            else:worerr = worerr + 1
            errnum = errnum + 1
            whichlist.append([preY[i],errnum])
        else:whichlist.append([preY[i],0])
    errnumrate = float(errnum)/len(preY)
    errMat = [a11,a12,a21,a22]
    return errMat,errnumrate,whichlist

def forate(errMat):
    #用于返回特异度灵敏度一系列
    a11=errMat[0]
    a12=errMat[1]
    a21=errMat[2]
    a22=errMat[3]
    mingandu=float(a11)/(a11+a12)
    teyidu=float(a22)/(a21+a22)
    posidu=float(a11)/(a11+a21)
    negdu=float(a22)/(a12+a22)
    return mingandu,teyidu,posidu,negdu

def AUC(Y,preY):
    import numpy as np
    from sklearn import metrics
    fpr,tpr,thresholds = metrics.roc_curve(Y,preY,pos_label=1)
    auc = metrics.auc(fpr,tpr)
    return auc

def list2xls(list):
    file = open('x.csv','w')
    file.write(str(list));
    file.close()