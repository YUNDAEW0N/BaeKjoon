import sys
input=sys.stdin.readline

N,K=map(int,input().split())

coins=[]
for i in range(N):
    A=int(input())
    coins.append(A)

coins.sort(reverse=True)
total=K

count=0
for coin in coins:
    if coin>total:
        continue

    count+=total//coin
    total=total%coin

print(count)