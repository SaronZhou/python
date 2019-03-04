# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:08:59 2019

@author: admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D


### scikit-learn库实现机器学习 ###

## iris数据集 ##
from sklearn import datasets
iris = datasets.load_iris()
iris.data
# 花卉的种类 
iris.target
# 花卉类别
iris.target_names
# 数据集的第一、二列为萼片的长和宽，第三、四列为花瓣的长和宽
x = iris.data[:, 2]
y = iris.data[:, 3]
species = iris.target

x_min, x_max = x.min() - .5, x.max() + .5
y_min, y_max = y.min() - .5, y.max() + .5

plt.figure()
plt.scatter(x, y, c=species)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())


# 主成分分解 #
from sklearn.decomposition import PCA
# fit_transform()函数用来降维，n_components表示降维后的主成分个数
x_reduced = PCA(n_components=3).fit_transform(iris.data)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x_reduced[:, 0], x_reduced[:,1], x_reduced[:,2], c=species)
ax.set_xlabel("First eigenvector")
ax.set_ylabel("Second eigenvector")
ax.set_zlabel("Third eigenvector")
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())


## K-近邻分类器 ##
from sklearn.neighbors import KNeighborsClassifier
np.random.seed(0)
iris = datasets.load_iris()
x = iris.data
y = iris.target
# permutation()函数打乱数据集所有的元素，前140条作为训练集，后10条作为测试集
i = np.random.permutation(len(iris.data))
x_train = x[i[: -10]]
y_train = y[i[: -10]]
x_test = x[i[-10: ]]
y_test = y[i[-10: ]]
# 调用分类器构造函数
knn = KNeighborsClassifier()
# 使用fit()函数对其进行训练
knn.fit(x_train, y_train)
knn.predict(x_test)
y_test

# 绘制决策边界
# 散点图为实际的点，绘制的边界为预测边界
import matplotlib as mat
x = iris.data[:, :2]
y = iris.target
x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5
y_min, y_max = x[:,1].min() - .5, x[:,1].max() + .5
cmap_light = mat.colors.ListedColormap(['#AAAAFF', '#AAFFAA', '#FFAAAA'])
h = .02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
knn = KNeighborsClassifier()
knn.fit(x, y)
# c_将参数左右相接，r_将参数上下相接
Z = knn.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
# Z代表分类的结果
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)


## Diabetes数据集 ##
diabetes = datasets.load_diabetes()
diabetes.data[0]
# 每一个数据都经过了均值化中心处理，又用标准差乘以个体数量调整了数值范围
np.sum(diabetes.data[:,0]**2)
diabetes.target


## 线性回归：最小平方回归 ##
from sklearn import linear_model
linreg = linear_model.LinearRegression()
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
linreg.fit(x_train, y_train)
linreg.coef_
linreg.predict(x_test)
# 以方差为评级指标，方差越接近于1，预测结果越准确
linreg.score(x_test, y_test)

# 年龄和病情之间的线性回归
x0_test = x_test[:, 0]
x0_train = x_train[:, 0]
# 存在np.newaxis的位置增加数组维数1
# 一行变为一列
x0_test = x0_test[:, np.newaxis]
x0_train = x0_train[:, np.newaxis]
linreg.fit(x0_train, y_train)
y = linreg.predict(x0_test)
plt.scatter(x0_test, y_test, color='k')
plt.plot(x0_test, y, color='b', linewidth=3)

plt.figure(figsize=(8,12))
for f in range(0,10):
    xi_test = x_test[:,f]
    xi_train = x_train[:, f]
    xi_test = xi_test[:, np.newaxis]
    xi_train = xi_train[:, np.newaxis]
    linreg.fit(xi_train, y_train)
    y = linreg.predict(xi_test)
    plt.subplot(5, 2, f+1)
    plt.scatter(xi_test, y_test, color='k')
    plt.plot(xi_test, y, color='b', linewidth=3)


## 支持向量机 ##
from sklearn import svm
x = np.array([[1,3], [1,2], [1,1.5], [1.5,2], [2,3], [2.5,1.5], [2,1], [3,1], [3,2], [3.5,1], [3.5,3]])
y = [0]*6 + [1]*5
plt.scatter(x[:,0], x[:,1], c=y, s=50, alpha=0.9)
svc = svm.SVC(kernel='linear').fit(x,y)
X,Y = np.mgrid[0:4:200j,0:4:200j]
Z = svc.decision_function(np.c_[X.ravel(),Y.ravel()])
Z = Z.reshape(X.shape)
plt.contourf(X,Y,Z>0, alpha=0.4)
plt.contour(X,Y,Z,colors=['k'], linestyles=['-'],levels=[0])
plt.scatter(x[:,0], x[:,1], c=y, s=50, alpha=0.9)






