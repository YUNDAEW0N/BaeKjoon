import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    N=int(input()) 

    dp1=[0]*(N+2)
    dp1[0]=1
    dp1[1]=2
    dp1[2]=4
    for i in range(3,N+1):
        dp1[i]=dp1[i-1]+dp1[i-2]+dp1[i-3]

    print(dp1[N-1])