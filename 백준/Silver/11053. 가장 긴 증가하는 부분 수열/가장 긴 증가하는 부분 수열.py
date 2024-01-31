import sys
input=sys.stdin.readline

N=int(input())
arr=[0]+list(map(int, input().split()))

#dp 테이블 생성및 초기화
dp=[0]*(N+1)



for i in range(1,N+1):
    mx=0
    for j in range(i):
        if arr[j]<arr[i]:
            mx=max(mx,dp[j])
    dp[i]=mx+1


print(max(dp))
