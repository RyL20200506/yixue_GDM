## -*- coding:utf-8 -*-
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def RatiofHave(pre):
    hangsize = len(pre)
    ratiofhave = 0
    have = 0
    for i in range(hangsize):
        if float(pre[i][0])>0:
            have = have + 1
        if float(pre[i][0])>0 and pre[i][1]!=0:
         ratiofhave = ratiofhave +1
        else:continue
    return ratiofhave/float(have)

def RatiofZero(pre):
    hangsize = len(pre)
    ratiofzero = 0
    zero = 0
    for i in range(hangsize):
        if float(pre[i][0])<0:
            zero = zero + 1
        if float(pre[i][0])<0 and pre[i][1]!=0:
         ratiofzero = ratiofzero +1
        else:continue
    return ratiofzero/float(zero)

def list2figure(x,y):
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x[:,0],x[:,1],15.0*np.array(x),15.0*np.array(y))
    plt.show()


def Csv2list(filename,a,b):
    import csv
    filename='cle000792.csv'
    reader = csv.reader(open(filename))
    list = []
    i = 0
    #a = 1
    #b = 50
    for items in reader:
        if i>=a and i <=b:
            list.append(float(items[3])-1)
            i = i+1
        else:
            i=i+1
        print i
    return  list

def Csv2shoupan(filename,a,b):
    import csv
    filename = 'cle000792.csv'
    reader = csv.reader(open(filename))
    list = []
    i = 0
    # a = 1
    # b = 50
    for items in reader:
        if i >= a and i <= b:
            list.append(float(items[2]))
            i = i + 1
        else:
            i = i + 1
        print i
    return list

def gui1hua(list):
    max0 = float(max(list))
    min0 = float(min(list))
    list1 = []
    for i in range(len(list)):
        list1.append((list[i]-min0)/(max0-min0))
    return list1

def gui1hua_yi(list):#将每一列向量进行归一化
    liesize = len(list[0])
    list4 = []
    for j in range(liesize):
        list2 = [list1[j] for list1 in list]
        list3 = gui1hua(list2)
        list4.append(list3)
    list5 = np.array(list4).transpose()
    return list5.tolist()

def ratio2XLabel(ratio,m):#m表示自变量的个数，即用几天的数据来进行判断
    X = []
    label = []
    for i in range(len(ratio)-m):
        if ratio[i]>=0:label.append(1)
        else:label.append(-1)

        forX = []
        for j in range(1,m+1):
            forX.append(ratio[i+j])
        X.append(forX)
    return X,label

def shoupan2XLabel(shoupan,m):#m表示自变量的个数，即用几天的数据来进行判断
    X = []
    label = []
    for i in range(len(shoupan)-m-1):
        if shoupan[i]-shoupan[i+1]>=0:label.append(1)
        else:label.append(-1)

        forX = []
        for j in range(1,m+1):
            forX.append(shoupan[i+j])
        X.append(forX)
    return X,label

def list2cav(filename,pre1):
    csvact = filename  # 这是文件的名字
    with open(csvact, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(pre1)