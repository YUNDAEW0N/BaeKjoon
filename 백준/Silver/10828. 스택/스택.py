#스택 구현하기
import sys
input=sys.stdin.readline

class Stack:
    def __init__(self,capacity: int=256):
        self.capacity=capacity
        self.ptr=0
        self.stk=[None]*capacity

    
    def push(self,value: int):
        self.stk[self.ptr]=value
        self.ptr+=1
       

    def pop(self)->int:
        if self.ptr==0:
            print(-1)
        else:
            self.ptr-=1
            print(self.stk[self.ptr])
        

    def size(self)->int:
        print(self.ptr)
        
    def empty(self)->int:
        if self.ptr==0:
            print(1)
        else:
            print(0)
            
    def top(self)->int:
        if self.ptr==0:
            print(-1)
        else:
            print(self.stk[self.ptr-1])
        
ls=[]
T=int(input())
stack=Stack(T)


for i in range(T):
    s=input().split()

    if s[0]=='push':
        stack.push(int(s[1]))
    elif s[0]=='pop':
        stack.pop()
    elif s[0]=='size':
        stack.size()
    elif s[0]=='empty':
        stack.empty()
    elif s[0]=='top':
        stack.top()
    

    
