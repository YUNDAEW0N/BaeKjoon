#큐 구현하기

import sys

input=sys.stdin.readline

class Queue:

    def __init__(self,capacity: int =256):
        self.que=[None]*capacity
        self.front=0
        self.rear=0
        self.no=0
        self.capacity=capacity

    def push(self,value: int):
        self.que[self.rear]=value
        self.rear+=1
        self.no+=1
        if self.rear==self.capacity:
            self.rear=0
    
    def pop(self):
        if self.no>0:
            x=self.que[self.front]
            self.front+=1
            if self.front==self.capacity:
                self.front=0
            print(x)
            self.no-=1
        else:
            print(-1)
            
    def size(self):
        print(self.no)
    
    def empty(self):
        if self.no==0:
            print(1)
        else:
            print(0)
    
    def pfront(self):
        if self.no==0:
            print(-1)
        else:
            print(self.que[self.front])

    def back(self):
        if self.no==0:
            print(-1)
        else:
            print(self.que[self.rear-1])

        
T=int(input())
que=Queue(T)


for i in range(T):
    s=input().split()

    if s[0]=='push':
        que.push(int(s[1]))
    elif s[0]=='pop':
        que.pop()
    elif s[0]=='size':
        que.size()
    elif s[0]=='empty':
        que.empty()
    elif s[0]=='front':
        que.pfront()
    elif s[0]=='back':
        que.back()

