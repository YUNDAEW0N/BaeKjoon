import sys
input=sys.stdin.readline


def dfs(n,sum,cnt):
    global ans
    #종료조건(n에 관련) + 정답관련 처리
    if n==N:
        if sum==S and cnt>0:
            ans+=1
        return
    
    #포함하는 경우
    dfs(n+1,sum+list[n],cnt+1)
    #포함하지 않는 경우
    dfs(n+1,sum,cnt)



N,S=map(int,input().split())
list=list(map(int,input().split()))

ans=0
dfs(0,0,0)
print(ans)
