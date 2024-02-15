import sys
from collections import deque

input = sys.stdin.readline

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = True
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = True

def solv():
    answer = 0  # 각 테스트 케이스마다 배추 구역의 개수를 저장할 변수
    for i in range(n):
        for j in range(m):
            if not v[i][j] and arr[i][j] == 1:
                bfs(i, j)
                answer += 1  # 배추 구역을 발견할 때마다 개수를 증가시킴
    print(answer)

T = int(input())

for _ in range(T):
    m, n, c = map(int, input().split())  
    arr = [[0] * m for _ in range(n)]  
    v = [[False] * m for _ in range(n)]  
    for _ in range(c):
        y, x = map(int, input().split())  
        arr[x][y] = 1
    solv()
