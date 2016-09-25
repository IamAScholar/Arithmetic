#coding=utf8
'''
容错处理
Created on 2016��9��25��

@author: LI
'''
class Queue:
    q=[0]*10
    tail=0;
    head=0;
    def __init__(self):
        pass
    def enQueue(self,x):
        self.q[self.tail]=x
        if self.tail == len(self.q)-1:
            self.q.tail=0
        else:
            self.tail=self.tail+1
    
    def deQueue(self):
        x=self.q[self.head]
        if self.head == len(self.q)-1:
            self.head=0
        else:
            self.head=self.head+1
        return x
            
if __name__ =="__main__":
    q=Queue()
    q.enQueue(1)
    q.enQueue(2)
    print q.deQueue()
    q.enQueue(5)
    print q.q
    print q.deQueue()
    
