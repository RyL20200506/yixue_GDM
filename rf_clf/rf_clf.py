# -*- coding:utf-8 -*-
#用来导入已保存分类器，并做出预测
#Author：Ry.L

from sklearn.externals import joblib

#一下是需要手动输入的年龄，身高，体重，空腹血糖
age = 26
height = 1.6
weight = 70
OGTT = 4.9
#=============================================
clf = joblib.load("rf.m")
BMI = weight/(height**2)
prediction = clf.predict([[age,BMI,OGTT,height,weight]])
possible = clf.predict_proba([[age,BMI,OGTT,height,weight]])
huanbingpossible = possible[0][1]
print huanbingpossible #输出的就是患病的概率
#-1没病，１有病