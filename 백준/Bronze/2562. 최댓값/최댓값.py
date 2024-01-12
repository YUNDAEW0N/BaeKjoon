a=[]


for i in range(9):
    b=int(input())
    a.append(b)

maximum=a[0]
max_index=1

for i in range(1,len(a)):
    if a[i]>maximum:
        maximum=a[i]
        max_index=i+1


print("%d\n%d"%(maximum,max_index))