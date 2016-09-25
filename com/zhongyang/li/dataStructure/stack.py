#coding=utf8
'''
Created on 2016年9月25日

@author: LI
'''
from _ctypes import Array

class Stack:
    S=[]
    top=-1
    def __init__(self):
        pass
    
    def stackEmpty(self):
          if self.top==-1:
              return True
          else:
              return False
    def push(self,x):
        self.top=self.top+1
        self.S.append(x)
    def pop(self):
        if self.stackEmpty():
            return "underflow"
        else:
            self.top=self.top-1
            return self.S[self.top+1]
if __name__=='__main__':
    s=Stack()
#     print s.stackEmpty()
    s.push(1)
    s.push(3)
    print s.pop()
    print s.pop()
    print s.pop()
   
    
