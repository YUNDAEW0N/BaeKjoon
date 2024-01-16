from typing import Any
import sys
input=sys.stdin.readline

class Queue:

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def enque(self, x: Any) -> None:
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def __bool__(self) -> bool:
        return self.no > 0

n, k = map(int, input().split())
que = Queue(n)
answer = []

for i in range(n):
    que.enque(i + 1)

while que:
    for i in range(k):
        x = que.deque()
        if i<k-1:
            que.enque(x)
        
    answer.append(x)


print(f'<{", ".join(map(str, answer))}>')
