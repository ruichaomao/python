#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
最小二乘法  This program is to obtain the r of the circle
"""

from numpy import *
from scipy import optimize
ff = open('xy.dat','r').readlines()
file = open('r.dat','w')
for i in ff:
    x_list1 = i.strip().split('---')[0].split()
    y_list1 = i.strip().split('---')[1].split()
    x_list = [float(i) for i in x_list1]
    y_list = [float(i) for i in y_list1]

    x = x_list 
    y = y_list

    def calc_R(xc, yc):
        #计算s数据点与圆心(xc, yc)的距离
        return sqrt((x - xc) ** 2 + (y - yc) ** 2)

    def f_2(c):
        #计算半径残余
        Ri = calc_R(*c)
        return Ri - Ri.mean()
            
    def coupR(x=[],y=[]):
        x_m = mean(x)
        y_m = mean(y)
        #圆心估计
        center_estimate = x_m,y_m
        center_2, _ = optimize.leastsq(f_2, center_estimate)
        xc_2, yc_2 = center_2
        #拟合圆的半径
        Ri_2       = calc_R(xc_2,yc_2)
        R_2        = Ri_2.mean()
        return (R_2)
    aa = coupR(x,y)
    print (aa)
    file.write(str(aa)+'\n')
file.close()
