import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    N=int(input())
    coins=list(map(int,input().split()))
    goal=int(input())
    dp=[[0] * (goal+1) for _ in range(N)]
    dp[0][0]=1

    for i in range(N):
        for j in range(goal+1):
            if i>0:
                dp[i][j]+=dp[i-1][j]
            
            if j>=coins[i]:
                dp[i][j]+=dp[i][j-coins[i]]
    
    print(dp[N-1][goal])
    