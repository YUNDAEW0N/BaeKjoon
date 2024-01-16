import sys
input=sys.stdin.readline


N=int(input()) #탑의 개수
top_list=list(map(int,input().split()))  # 탑 리스트
stack=[]
answer=[0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1]>top_list[i]:
            answer[i]=stack[-1][0]+1
            break
        else:
            stack.pop()

    stack.append([i,top_list[i]])

print(*answer)




    
        
   