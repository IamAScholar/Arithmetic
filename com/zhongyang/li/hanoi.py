#coding=utf8
'''
Created on 2016年8月30日
递归算法，分解问题，分解后，将具体问题抽象，
@author: Administrator
'''
global i
i=1
def move(fr,des,n):
    global i
    print "第%u步，%u号盘 from %s to %s " %(i,n,fr,des)
    i+=1
def hanoi(a,b,c,n):
    if(n==1):
        move(a,c,n)
        return
    hanoi(a,c,b,n-1)
    move(a,c,n)
    hanoi(b,a,c,n-1)


if __name__ == "__main__":
    hanoi("A","B","C",2)