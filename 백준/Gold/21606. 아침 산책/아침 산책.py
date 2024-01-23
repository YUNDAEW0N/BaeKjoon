import sys
input=sys.stdin.readline

N=int(input())
A=input().rstrip()
info=[[int(digit)] for digit in A]
info=[[]]+info


count=0

graph=[[] for _ in range(N+1)]

for i in range(N-1):
    n,m=map(int,input().split())
    graph[n].append(m)
    graph[m].append(n)
    graph[n].sort()
    graph[m].sort()

# print(graph)
# print(info)


def dfs(graph, start):
    visited=set()
    stack=[start]
    global count
    while stack:
        now=stack.pop()
        if now not in visited:
            # print(f'start{start} now{now} graph[now]{graph[now]}') 
            visited.add(now)
            stack.extend(reversed(graph[now]))
            if info[now][0]==1 and now!=start:
                count+=1
                               
    
    return visited


for i in range(1,N+1):
    if info[i][0]==1:
        dfs(graph,i)
        # print(count) 
        
print(count)
