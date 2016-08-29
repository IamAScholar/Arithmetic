#coding=utf8
'''
Created on 2016年8月29日

@author: Administrator
'''
import util
def counting_sort(a,b):
    c=[0]*util.max(a)
    for i in range(0,len(a)):
        c[a[i]]+=1
    for i in range(1,len(c)):
        c[i]=c[i]+c[i-1]  #计算x前面有多少位
    for i in range(0,len(a)):
        b[c[a[i]]-1]=a[i] #从零开始，数组越界问题
        c[a[i]]=c[a[i]]-1


if __name__ == "__main__":
    a=util.getNumber(20)
    b=[0]*len(a)
    print a
    counting_sort(a,b)
    print b
        
