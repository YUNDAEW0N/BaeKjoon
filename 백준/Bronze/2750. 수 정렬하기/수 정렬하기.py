T=int(input())
arr=[]

for i in range(T):
    n=int(input())
    arr.append(n)


def quick_sort(arr,left: int,right: int):
    pl=left
    pr=right
    pivot=arr[(pl+pr)//2]

    while pl<=pr:
        while arr[pl]<pivot:
            pl+=1
        while arr[pr]>pivot:
            pr-=1
          
        if pl<=pr:
            arr[pl],arr[pr]=arr[pr],arr[pl]
            pl+=1
            pr-=1
    if left<pr:
        quick_sort(arr,left,pr)
    if pl<right:
        quick_sort(arr,pl,right)


quick_sort(arr,0,T-1)

for i in range(len(arr)):
    print(f'{arr[i]}')
           

    