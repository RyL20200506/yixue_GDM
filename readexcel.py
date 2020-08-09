# -*- coding: utf-8 -*-
#print 'hello world'

#先来一个读取excel的程序
import xlrd

def readxls(xlsname):#要求xlsname是一个字符串

    data = xlrd.open_workbook(xlsname) #打开这个字符串
    table = data.sheets()[0] #打开第一张表
    nrows = table.nrows #获取表的行数
    colmns = table.ncols #获取表的列数
    all = [] #用于存储所有的数据
    for i in range(nrows):
        if i<3:
            continue
        all.append(table.row_values(i)[:])
    return all

def clc(list): #list是待清理list
    import numpy as np
    hangsize = len(list)
    liesize = len(list[0])
    list2 = []
    for i in range(hangsize-1):
        if float(list[i][liesize-1])==0:
            list[i][liesize - 1]=-1
        for j in range(liesize-1):
            if list[i][j] !='':
                if j ==liesize-2:
                    list2.append(list[i])
                else: continue
            else:
                break
    print (len(list2))
    print (len(list2[0]))

    file = open('zibianliang.txt','w')
    file.write(str(list));
    file.close()
    return list2

#将数据重新写成excel
#def write()

def list2XY(list,forx):#默认是在最后一列
    X = []
    Y = []
    hangsize = len(list)
    liesize = len(list[0])
    for i in range(hangsize):
        Y.append(float(list[i][liesize-1]))
        forX = []
        for j in forx:
            forX.append(list[i][j])
        X.append(forX)
    return X,Y


