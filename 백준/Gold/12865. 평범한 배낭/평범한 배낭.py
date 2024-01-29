import sys
input=sys.stdin.readline

N,K=map(int,input().split())

dp=[[0]*(N+1) for _ in range(K+1)]
items=[(0,0)]




for i in range(N):
    w,v=map(int,input().split())
    items.append((w,v))



for i in range(1,N+1):
    for j in range(1,K+1):
        if j>=items[i][0]:
            dp[j][i] = max(dp[j][i-1], dp[j-items[i][0]][i-1] + items[i][1])
        else:
            dp[j][i]=dp[j][i-1]


print(dp[K][N])