n=int(input())

pos=[0]*n  #퀸 배치 포지션
flag_a=[False]*n
flag_b=[False]*(n*2-1)
flag_c=[False]*(n*2-1)

count=0

def Queen(i :int):
    global count
    for j in range(n):
        if( not flag_a[j] and
            not flag_b[i+j] and
            not flag_c[i-j+(n-1)]):
            pos[i]=j
            if i==n-1:
                count+=1
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+(n-1)]=True
                Queen(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+(n-1)]=False


Queen(0)
print(count)