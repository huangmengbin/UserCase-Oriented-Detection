# -*- coding: utf-8 -*-
"""
Created on Jan 14 2020
@author: wanggang
功能：根据数据的大小画出柱状图的颜色来。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
plt.rcParams['axes.unicode_minus']=False     # 正常显示负号
divLine=0.8
x = np.array(["稽查","流程","核实","问题","现场","质量","管理","用户","系统","整改"])  # x值取默认值
y = np.array([0.2, 0.3, 0.17, 0.9, 0.8, 0.7, 0.32, 0.89, 0.91, 0.46])

sortIndex = np.argsort(-y) # 倒序，返回排序后各数据的原始下标

x_sort = x[sortIndex] # 重新进行排序，与y保持初始顺序一致
y_sort = y[sortIndex] # 重新进行排序，倒序

#定义函数来显示柱上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.25, 1.01*height, '%s' % int(height))
print(y_sort)
plt.xticks(np.arange(len(x_sort)), x_sort)
for i in range(len(y_sort)):
    if y_sort[i] >divLine:
        plt.bar(x_sort[i],y_sort[i],color=['r'])
    else:
        plt.bar(x_sort[i], y_sort[i], color=['g'])
#a = plt.bar(np.arange(len(x_sort)),y_sort,color=['r','g','b', 'c', 'm', 'y'])#这是设置颜色的
#autolabel(a)

plt.title('top10')
plt.ylabel('词频', fontsize=12)
plt.xlabel('词语', fontsize=12)
plt.show()