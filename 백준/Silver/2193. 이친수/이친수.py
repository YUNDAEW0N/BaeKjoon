import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(N+3)
dp[1]=1
dp[2]=1
dp[3]=2

for i in range(4,N+1):
    dp[i]=dp[i-2]+dp[i-1]

print(dp[N])