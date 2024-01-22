import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
ans=0

for i in range(M):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start):
    stack=[start]
    global ans
    while stack:
        now=stack.pop()
        
        if visited[now]==False:
            visited[now]=True
            ans+=1
            stack.extend(reversed(graph[now]))


dfs(graph,1)
print(ans-1)


    