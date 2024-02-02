import sys
input=sys.stdin.readline

N=int(input())

for j in range(N-1):
    print(" "*(N-(j+1))+"*"*((j*2)+1))

for i in range(N):
    print(" "*i+"*"*(((N-i)*2)-1))