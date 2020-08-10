# 偏航样本较小，故基于KNN-最近邻算法方法进行最佳导航系统预测
# Ry.L Date:2020年8月9日

'''
Refer:
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
'''

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def RGB_to_Hex(rgb):
    RGB = rgb
    color = '#'
    for i in RGB:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color


def Hex_to_RGB(hex):
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    rgb = (r, g, b)
    return rgb


# Training Part
## Loading data
data = pd.read_csv('data.txt', sep='\\s+')
train_index = data.loc[:, ['风向参数x', '风向参数y']].values
train_label0 = data.loc[:, ['对应的最佳偏航模式']].values
train_label = np.reshape(train_label0, len(train_label0))
## Training
neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')  # weights可以尝试用'distance'
neigh.fit(train_index, train_label)

# Verification Part
data_vef = pd.read_csv('data_vef.txt', sep='\\s+')
ver_index = data_vef.loc[:, ['风向参数x', '风向参数y']].values
ver_label0 = data_vef.loc[:, ['对应的最佳偏航模式']].values
ver_label = np.reshape(ver_label0, len(ver_label0))

result = neigh.predict(ver_index)
print('测试集:', data_vef)
print('测试结果:', result)
print('模型准确率', neigh.score(ver_index, ver_label))

# Visualization
plt.figure()
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
num2colors_dict = {i+1: colors[i] for i in range(len(colors))}
color_list_dot = []
color_list_bac = []

## Preparation
for i in range(1, max(data['对应的最佳偏航模式'].values)+1):
    if len(data[data['对应的最佳偏航模式'] == i])>0:
        color_list_bac.append(num2colors_dict[i])

## Background classify
xx, yy = np.meshgrid(np.arange(min(train_index[:, 0])-1, max(train_index[:, 1]+1), 0.1),
                     np.arange(min(train_index[:, 0])-1, max(train_index[:, 1]+1), 0.1))
coords = np.c_[xx.ravel(), yy.ravel()]
Z = neigh.predict(coords)
Z = Z.reshape(xx.shape)
light_rgb = matplotlib.colors.ListedColormap(color_list_bac)
plt.pcolormesh(xx, yy, Z, cmap=light_rgb)

## Scatter
for i in range(1, max(data['对应的最佳偏航模式'].values)+1):
    if len(data[data['对应的最佳偏航模式'] == i])>0:
        dot_color = RGB_to_Hex(Hex_to_RGB(num2colors_dict[i]) + np.array([-50, -50, -50]))
        plt.scatter(data[data['对应的最佳偏航模式'] == i].iloc[:, 0], data[data['对应的最佳偏航模式'] == i].iloc[:, 1], c=dot_color, label=str(i))
plt.legend()





