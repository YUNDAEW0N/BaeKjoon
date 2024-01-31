import sys
input=sys.stdin.readline

n=int(input())
a=[int(input()) for _ in range(n)]
total=sum(a)

dp=[0]*(n+1)
if n==3:
    print(total-min(a[0],a[1]))
    exit()
elif n<3:
    print(total)
    exit()
dp[0]=a[0]
dp[1]=a[1]
dp[2]=a[2]
for i in range(3,n):
    dp[i]=min(dp[i-2]+a[i],dp[i-3]+a[i])


minimum=min(dp[n-2],dp[n-3])
print(total-minimum)
# print(dp)
