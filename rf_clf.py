# -*- coding:utf-8 -*-
#用来导入已保存分类器，并做出预测
#Author：Ry.L

from sklearn.externals import joblib

#一下是需要手动输入的年龄，身高，体重，空腹血糖
age = 26
height = 1.57
weight = 56
OGTT = 4.51
#=============================================
clf = joblib.load("rf.m")
BMI = weight/(height**2)
prediction = clf.predict([[age,BMI,OGTT,height,weight]])
possible = clf.predict_proba([[age,BMI,OGTT,height,weight]])
print prediction,possible
#-1没病，１有病


