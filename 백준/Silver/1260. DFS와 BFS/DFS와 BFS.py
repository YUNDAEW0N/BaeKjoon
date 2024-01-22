import sys
from collections import deque

input=sys.stdin.readline

N,M,V=map(int, input().split()) # N 노드의갯수 M 간선의 갯수 V 출발노드

graph=[[] for _ in range(N+1)]   # 인접노드 저장할 그래프

#양방향이니까 각 인접노드들 그래프에 넣어주기
for i in range(M):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

#dfs 구현
def dfs(graph,start): # 탐색할 그래프와 출발지점을 파라미터로 받는다.
    visited=set()        # 방문을 체크할 리스트
    route=[]          # 실제 지나간 경로를 저장할 배열 
    stack=[start]     # 스택을 이용해서 경로를 찾는다. (출발지 미리 셋팅)
    
    while stack:      # 스택에 데이터가 빌때까지 반복
        now=stack.pop()   # 현재노드를 스택에서 받아온다.
        if now not in visited:  # 현재노드를 방문한적이 없다면
            route.append(now)   #지나간 경로에 저장
            visited.add(now)    #방문했다고 체크
            stack.extend(reversed(graph[now])) # 스택에 현재노드의 인접노드들 푸쉬 (stack은 LIFO 구조라 리버스로 꺼꾸로넣는다)
            # 또한 그래프에 [a,b] 형식으로 들어가있어서 스택에 넣을때 extend로 압축풀어서 넣어야한다.
    return route



#bfs 구현
def bfs(graph, start):  #탐색할 그래프, 출발지점 파라미터로 받기
    visited=set()       #방문체크리스트
    route=[]            #지나간 경로 저장
    queue=[]            #큐를 이용해 경로찾기

    queue.append(start)   # 큐에 시작점 추가
    visited.add(start)    # 출발점도 방문한거니까 추가

    while queue:             # 큐가 빌때까지
        now=queue.pop(0)     # 현재노드에 큐에서팝한 데이터 가져오기
        route.append(now)    # 지나간 경로에도 넣어주고
        for neighbor in graph[now]:      # 인접노드들을 확인
            if neighbor not in visited:  # 만약 인접노드가 방문한적이 없으면
                visited.add(neighbor)         # 방문배열에 인접노드 추가
                queue.append(neighbor)        # 큐에 인접노드 추가
        # print(queue)

    return route

    
print(*dfs(graph,V)) 
print(*bfs(graph,V))



    
    

