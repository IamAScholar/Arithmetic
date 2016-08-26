#coding=utf8
'''
Created on 2016年8月26日

@author: Administrator
'''
import random
def getNumber(length):
    a = [1]*length
    for i in range(0, length) :
        a[i] = random.randint(-15, 15)
    return a
def exchange(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp