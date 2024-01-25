import sys
input=sys.stdin.readline

N=int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    A= input().rstrip()
    row = [int(a) for a in A]
    graph[i] = row




v=[[False]*N for _ in range(N)]
house=[]

def bfs(si,sj,ei,ej):
    q=[]
    
    count=0
    v[si][sj]=True
    q.append((si,sj))

    while q:
        ci,cj=q.pop(0)
        count+=1

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=di+ci,dj+cj
            if 0<=ni<N and 0<=nj<N and graph[ni][nj]==1 and v[ni][nj]==False:
                q.append((ni,nj))
                v[ni][nj]=True
                
        
    return count


for i in range(N):
    for j in range(N):
        if not v[i][j] and graph[i][j]==1:
            count=bfs(i,j,N-1,N-1)
            house.append(count)

print(len(house))
house.sort()
for i in range(len(house)):
    print(house[i])
