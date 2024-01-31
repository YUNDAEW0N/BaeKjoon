import sys
input=sys.stdin.readline

N,M=map(int,input().split())

arr=[0]+list(map(int, input().split()))
# print(arr)
dp=[0]*(N+1)

for i in range(1,N+1):
    dp[i]=arr[i]+dp[i-1]


# print(dp)

for i in range(M):
    s,e=map(int,input().split())

    print(dp[e]-dp[s-1])