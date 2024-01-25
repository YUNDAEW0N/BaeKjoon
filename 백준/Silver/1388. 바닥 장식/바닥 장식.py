import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N):
    digit = input().rstrip()
    # '-'를 1로, '|'를 0으로 변환하여 행에 추가
    row = [1 if a == '-' else 0 for a in digit]
    graph[i] = row

cnt=0
count=0


#열먼저 검사
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and (j + 1 < len(graph[i])) and graph[i][j + 1] != 1:
            count+=1
            # print(f'count{i} :{count}')
        #한줄이 다 1일때
        elif graph[i][j]==1:
            if j==M-1:
                count+=1
                continue
            cnt+=1
            if cnt==M:
                count+=1
    cnt=0


#행 검사
for j in range(M):
    for i in range(N):
        if graph[i][j] == 0 and (i + 1 < N) and graph[i+1][j] != 0:
            count+=1    
        #한줄이 다 0일때
        elif graph[i][j]==0:
            if i==N-1:
                count+=1
                continue
            cnt+=1
            if cnt==N:
                count+=1
                
    cnt=0




print(count)

# 50퍼에서 틀렸습니다 나옴...ㅋ