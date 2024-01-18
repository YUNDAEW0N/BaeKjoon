# WEEK01 TEST
import sys
input=sys.stdin.readline

#1 1110 더하기 사이클

T=int(input())
num=T
count=0


for i in range(99):
  
    x=(num//10)+num%10
    if x>=10:
        num=(num%10)*10+(x%10)
    else:
        num=(num%10)*10+x

    count+=1
    if num==T:
        break

print(count)


