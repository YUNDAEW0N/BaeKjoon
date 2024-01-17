import sys
input=sys.stdin.readline

T=int(input())
s=[]

for i in range(T):
    n=int(input())
    s.append(n)


s.sort()

for i in range(len(s)):
    print(s[i])