#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:29:47 2021

@author: laura
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.array([512,1024,2048,4096,8192,16384])
c01=np.array([2.233,2.217,2.218,2.215,2.216])
c1=np.zeros(6)
c2=np.zeros(6)
c3=np.zeros(6)
dp0=0.0
dp1=np.zeros(6)
dp2=np.zeros(6)
dp3=np.zeros(6)
c0=0.0
n=1.0/5.0
c02=np.matrix([[2.139,2.157,2.143,2.159,2.145],
               [2.132,2.129,2.128,2.268,2.228],
               [2.134,2.137,2.135,2.135,2.137],
               [2.139,2.137,2.137,2.133,2.140],
               [2.133,2.136,2.136,2.133,2.136],
               [2.132,2.138,2.131,2.134,2.141]])
c03=np.matrix([[2.184,2.179,2.183,2.181,2.179],
               [2.168,2.170,2.178,2.173,2.165],
               [2.154,2.147,2.165,2.158,2.148],
               [2.156,2.144,2.146,2.139,2.143],
               [2.135,2.138,2.136,2.139,2.140],
               [2.137,2.132,2.135,2.132,2.141]])

for j in range(5):
    c0=c0+c01[j]*n
for j in range(5):
    dp0=dp0+((c01[j]-c0)**2.0)*n
dp0=dp0**(0.5)

for i in range(6):
    c1[i]=c0
    for j in range(5):
        c2[i]=c2[i]+c02[i,j]*n
        c3[i]=c3[i]+c03[i,j]*n

for i in range(6):
    dp1[i]=dp0
    for j in range(5):
        dp2[i]=dp2[i]+((c02[i,j]-c2[i])**2.0)*n
        dp3[i]=dp3[i]+((c03[i,j]-c3[i])**2.0)*n

for i in range(6):
    dp2[i]=dp2[i]**(0.5)
    dp3[i]=dp3[i]**(0.5)

linha1,=plt.plot(t,c1,label="Código original",color='red',ls='--')
linha2,=plt.plot(t,c2,label="Código com 1 modificação",color='blue',ls=':')
linha3,=plt.plot(t,c3,label="Código final",color='green',ls='-.')

plt.xlabel("TILE=VECLEN")
plt.ylabel("Tempo (s)")
plt.legend(handles=[linha1,linha2,linha3],loc='best')
plt.show() 

linha4,=plt.plot(t,dp1,label="Código original",color='red',ls='--')
linha5,=plt.plot(t,dp2,label="Código com 1 modificação",color='blue',ls=':')
linha6,=plt.plot(t,dp3,label="Código final",color='green',ls='-.')

plt.xlabel("TILE=VECLEN")
plt.ylabel("Desvio padrão")
plt.legend(handles=[linha4,linha5,linha6],loc='best')
plt.show() 


