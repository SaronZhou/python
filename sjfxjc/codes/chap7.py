# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:27:26 2019

@author: admin
"""

### 描述性统计与建模 ###
# 葡萄酒质量的描述性统计 #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
# pandas.DataFrame.columns得到数据框的列标签
wine.columns = wine.columns.str.replace(' ', '_')
# pd.DataFrame.head 默认的返回数据框的前5行
print(wine.head())
# 显示所有变量的描述性统计量
print(wine.describe())
# 找出列quality的唯一值
print(sorted(wine.quality.unique()))
# 计算唯一值的频率
print(wine.quality.value_counts())


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm
# 分组、直方图与t检验 #
# 按照葡萄酒类型显示质量的描述性统计量
# unstack函数将结果重新排列
print(wine.groupby('type')['quality'].describe().unstack('type'))
# 按照葡萄酒类型显示质量的第一、三四分位数
print(wine.groupby('type')['quality'].quantile([0.25, 0.75]).unstack('type'))
# 按照葡萄酒类型查看质量分布
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']
# set_style设定主题：darkgrid灰色网格、whitegrid白色网格、ticks十字叉、white、dark
sns.set_style('dark')
# 参数norm_hist为真，直方图高度显示密度分布，不显示频率分布，因为两组酒数据数目不同
print(sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red Wine'))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='White Wine'))
# sns.axlabel('Quality Score', 'Density')
plt.suptitle("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# 检验红葡萄酒与白葡萄酒的平均质量是否有所不同
# agg(['std'])按照标准差进行聚合
print(wine.groupby('type')['quality'].agg(['std']))
# ttest_ind默认两组数据方差齐性的，如果想要设置默认方差不齐，可以设置equal_var=False
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))


# 成对变量之间的关系和相关性
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 计算所有变量之间的相关矩阵
print(wine.corr())
# 从两组酒的数据中取出小样本进行绘图
def take_sample(data_frame, replace=False, n=200):
    # random.choice在data_frame.index(数据框的行标签）中有放回选取200个数，可以设定概率p
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
red_sample = take_sample(wine.loc[wine['type']=='red', :])
white_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([red_sample, white_sample])
# where满足条件设定为1，否则为0
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
# crosstab计算频数表，margin为真添加行列边缘
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

# 查看成对变量之间的关系
sns.set_style("dark")
# 参数palette用于映射色调变量的颜色集，如果是dict，键是hue变量中的值
# diag_kind主对角线及自己与自己比较的图形设定
# markers要么是用于所有数据点的标记，要么是长度与色调变量中的级别数相同的标记列表，这样不同颜色的点也会有不同的散点图标记。
# vars留哪些特征两两比较
# plot_kws/diag_kws设置具体参数更改
# ci:置信区间，x_jitter给x轴随机增加噪音点
g = sns.pairplot(wine_sample, kind='reg', plot_kws={'ci': False,\
            'x_jitter': 0.25, 'y_jitter': 0.25}, hue='type', diag_kind='hist',\
            diag_kws={'bins': 10, 'alpha': 1.0}, palette=dict(red='red', white='white'),\
            markers=['o', 's'], vars=['quality', 'alcohol', 'residual sugar'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=4,\
             horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
plt.show()


# 使用最小二乘估计进行线性回归 #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density\
                + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates\
                + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
# 或者可以使用广义线性回归
# lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
# 以序列形式返回模型系数
print("\nCoefficients:\n%s" % lm.params)
# 以序列形式返回模型系数的标准差
print("\nCoefficient Std Errors:\n%s" % lm.bse)
# 返回修正R方
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
# 返回F统计量与p值
print("\nF-statistic: %.1f P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
# 显示观测总数与拟合值总数
print("\nNumber of obs: %d Number of fitted values: %d" % (lm.nobs, len(lm.fittedvalues)))


# 自变量标准化 #
dependent_variable = wine['quality']
# 保存除了'quality', 'type', 'in_sample'外所有变量
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
# 对变量进行标准化
independent_variables_standarized = (independent_variables-independent_variables.mean()) / independent_variables.std()
wine_standarized = pd.concat([dependent_variable, independent_variables_standarized], axis=1)

# 重新线性回归
lm_standarized = ols(my_formula, data=wine_standarized).fit()
print(lm_standarized.summary())


# 预测 #
# 使用wine数据集前10个观测作为新的观测
new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
# 将预测值保留两位小数
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)