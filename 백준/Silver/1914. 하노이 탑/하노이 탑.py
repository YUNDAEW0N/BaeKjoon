def hanoi(N :int,start,target,help):
    #옮겨야 할 원판이 한개인 경우 시작기둥에서 목표기둥으로 옮긴다.
    if N==1:
        print(start, target)
    else:
        #덩어리그룹에서 바닥 원반을 제외하고 보조기둥으로 이동 ( 목표기둥을 보조기둥으로)
        hanoi(N-1,start,help,target)
        print(start, target)
        #보조기둥에 남은 바닥원반을 목표기둥으로 시작기둥을 이용해 옮긴다.
        hanoi(N-1,help,target,start)

    
 



N=int(input())
K=0

if N<=20:
    print(2**N-1)
    hanoi(N,1,3,2)
else:
    print(2**N-1)
    