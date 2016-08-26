#coding=utf8
'''
Created on 2016年8月26日

@author: Administrator
'''
import util
class heap:
    def __init__(self,a,heap_size):
        self.a=a
        self.heap_size=heap_size
    
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def exchange(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
def max_heapify(h,i): #关键在于max保存最大值下标，a[i]最大值
    max=i          
    if(left(i)<h.heap_size and h.a[i]<h.a[left(i)]):
        exchange(h.a, i, left(i))
        max=left(i)
    if(right(i)<h.heap_size and h.a[i]<h.a[right(i)]):
        exchange(h.a,i, right(i))
        max=right(i)
    if(i!=max):
       max_heapify(h,max)

def build_max_heap(h):
    for i in range(h.heap_size/2,-1,-1):
        max_heapify(h, i)
def sort_heap(h):
    build_max_heap(h)
    exchange(h.a, 0, h.heap_size-1)
    size=h.heap_size-1
    for i in range(0,size-2,1):
        build_max_heap(h)
        exchange(h.a, 0, h.heap_size-1)
        h.heap_size-=1

if __name__ == "__main__":
    a=util.getNumber(20)
#     a=[1,3,4,2,5,7,13,23]
    print a
    h=heap(a,len(a))
    sort_heap(h)
    #max_heapify(h,0)
    #build_max_heap(h)
    print a













    
