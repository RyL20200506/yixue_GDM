# 偏航样本较小，故基于KNN-最近邻算法方法进行最佳导航系统预测
# Ry.L Date:2020年8月9日

'''
Refer:
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
'''

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

# Training Part
data = pd.read_csv('data.txt', sep='\\s+')
train_set = data.loc[:, ['风向参数x', '风向参数y']].values

train_label0 = data.loc[:, ['对应的最佳偏航模式']].values
train_label = np.reshape(train_label0,len(train_label0))

neigh = KNeighborsClassifier(n_neighbors=3, weights='uniform')  # weights可以尝试用'distance'

neigh.fit(train_set, train_label)

# Verification Part
result = neigh.predict([[11.3910, 21.53630], [9.59540, 16.75], [9.93, 14.72]])
print('分类结果', result)




