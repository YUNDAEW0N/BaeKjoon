import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

graph=[]


for _ in range(N):
    row=list(map(int,input().split()))
    graph.append(row)




def bfs(si,sj,h):
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    while q:
        ci,cj=q.popleft()
        # 네방향, 범위내 , 미방문
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and graph[ni][nj]>h:
                q.append((ni,nj))
                v[ni][nj]=1
    



def solve(h):
    cnt=0
    for i in range(N):
        for j in range(N):
            if v[i][j]==0 and graph[i][j]>h:
                bfs(i,j,h)
                cnt+=1
    return cnt

ans=0
for h in range(100):
    v=[[0]*N for _ in range(N)]
    ans=max(ans,solve(h))
            

print(ans)