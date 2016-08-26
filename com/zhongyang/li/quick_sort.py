#coding=utf8
'''
Created on 2016年8月26日

@author: Administrator
'''
import util

def partition(a,left,right):
    x=a[right]
    i=left-1
    for j in range(left,right):
        if(a[j]>x):
            i+=1
            util.exchange(a, i, j)
    i+=1
    util.exchange(a, i, right)
    return i
def quick_sort(a,left,right):#递归
    if(left>right):
        return
    p=partition(a,left,right)
    quick_sort(a, left, p-1)
    quick_sort(a, p+1, right)


if __name__ == "__main__":
    a=util.getNumber(100)
    print a
    quick_sort(a, 0, len(a)-1)
    print a