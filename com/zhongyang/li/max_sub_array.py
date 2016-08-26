# coding=utf8
'''
Created on 2016年8月17日

@author: Administrator
'''

import array
import sys
import util


def max_cross_mid(a,mid,left,right):
    left_max_sum=-sys.maxint
    left_max=0
    sum=0
    for i in range(mid,left-1,-1):
        sum+=a[i]
        if(sum>=left_max_sum):
            left_max_sum=sum
            left_max=i
    right_max_sum=-sys.maxint
    right_max=0
    sum=0
    for i in range(mid+1,right+1,1):
        sum+=a[i]
        if(sum>=right_max_sum):
            right_max_sum=sum
            right_max=i
    max_sum=left_max_sum+right_max_sum
    return (max_sum,left_max,right_max)
def max_sub_array(a,left,right):
    #print a
    if(right==left):
        return (a[right],left,right)
    mid=(left+right)/2
    (left_max,left_left_max,left_right_max)=max_sub_array(a, left, mid)
    (right_max,right_left_max,right_right_max)=max_sub_array(a, mid+1, right)
    (cross_mid_max,cross_mid_left_max,cross_mid_right_max)=max_cross_mid(a,mid,left,right)
    if(left_max>=right_max and left_max>=cross_mid_max):
        return (left_max,left_left_max,left_right_max)
    if(right_max>=left_max and right_max>=cross_mid_max):
        return (right_max,right_left_max,right_right_max)
    if(cross_mid_max>=left_max and cross_mid_max>=right_max):
        return (cross_mid_max,cross_mid_left_max,cross_mid_right_max)


if __name__ == "__main__":
    # print ('This is Hello world!!')
    #print random.randint(-15, 15)
    num=util.getNumber(30)
   # num=[8, 15, 11, -5, -14, -14, -15, 3, 10, 0, 0, 4, -14, 12, -5, -14, 10, 7, -12, -4]
    print num
#     left_max_sum=-sys.maxint
#     print type(left_max_sum)
    print max_sub_array(num,0,len(num)-1)

   