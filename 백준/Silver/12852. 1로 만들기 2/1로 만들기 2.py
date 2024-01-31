import sys
input=sys.stdin.readline

N=int(input())

D=[0]*(N+1)



for i in range(2,N+1):
    D[i]=D[i-1]+1
    if i%2==0:
        D[i]=min(D[i],D[i//2]+1)
    if i%3==0:
        D[i]=min(D[i],D[i//3]+1)
print(D[N])

a=[N]
while N != 1:
    temp=D[N]
    if D[N-1]<temp:
        N-=1
        a.append(N)
    elif N%2==0 and D[N//2]<temp:
        N//=2
        a.append(N)
    elif N%3==0 and D[N//3]<temp:
        N//=3
        a.append(N)


print(' '.join(map(str, a)))