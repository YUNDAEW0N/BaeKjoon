import sys
input=sys.stdin.readline

N,M=map(int, input().split())
graph=[[] for _ in range(N+1)]

for i in range(M):
    a, b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)
count=0


def dfs(graph,start):
    
    stack=[start]

    while stack:
        now=stack.pop()
        if visited[now]==False:
            visited[now]=True
            stack.extend(reversed(graph[now]))
            # print(visited[now])

for i in range(1,N+1):
    if visited[i]==False:
        dfs(graph,i)
        count+=1


print(count)
