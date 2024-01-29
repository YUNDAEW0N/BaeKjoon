import sys
input=sys.stdin.readline

T=int(input())



for i in range(T):
    N=int(input())
    point=[0]*(N+1)
    for _ in range(N):
        a,b=map(int,input().split())
        point[a]=b
    count=0
    pivot=int(1e9)
    # print(f'point: {point}')    
    for j in range(1,len(point)):
        
        if pivot>point[j]:
            count+=1
            pivot=point[j]
            # print(f'pivot : {pivot}')
            # print(f'count: {count}')

    print(count)