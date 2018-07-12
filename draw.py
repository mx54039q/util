#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

def static():
  """
  折线图/点图:
  图/plot和axe/画线/边缘线框/图示/注释/坐标轴
  """
  # 创建图并设置大小/分辨率/背景颜色/背景边缘颜色/是否画边框等
  fig = plt.figure(figsize=(8,6), dpi=80,facecolor='white',edgecolor='red',frameon=True)
  # subplots/axes: plot必须规则排列, axe可以放在figure的任意位置
  #a1 = plt.subplot(211)
  #a2 = plt.subplot(212)
  #　函数输入输出对应横轴纵轴
  X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
  C,S = np.cos(X), np.sin(X)
  # 画线: 颜色/线宽/线类型/标签
  plt.plot(X, C, color="blue", linewidth=2.0, linestyle="-",label='cosine')
  plt.plot(X, S, "r-", linewidth=2.0,label='sine')
  #　对当前axe设置边缘线框
  ax = plt.gca() # get current axe
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.spines['bottom'].set_position(('data',0))
  ax.yaxis.set_ticks_position('left')
  ax.spines['left'].set_position(('data',0))
  # 设置图示
  plt.legend(loc='upper left', frameon=False)
  # 设置坐标轴范围/坐标轴节点
  plt.xlim(-4.0,4.0) # 横坐标范围
  plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
         [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])# 横坐标间隔
  plt.ylim(-1.0,1.0)
  plt.yticks([-1, 0, +1],
         [r'$1$', r'$0$', r'$-1$']) 
  # 注释说明
  t = 2*np.pi/3
  tt = np.linspace(-np.pi, np.pi, 16, endpoint=True)
  plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
  plt.scatter(tt,np.cos(tt), 50, color ='blue')
  plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
               xy=(t, np.sin(t)), xycoords='data',
               xytext=(+10, +30), textcoords='offset points', fontsize=16,
               arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

  plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
  plt.scatter(tt,np.sin(tt), 50, color ='red')
  plt.annotate(r'$cos$', xy=(t, np.cos(t)), xycoords='data',
               xytext=(-90, -50), textcoords='offset points', fontsize=16,
               arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
  # 显示图
  plt.show() # 显示图

def animation():
  """
  动画:
  
  """


