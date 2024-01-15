N=int(input())

def pactorial(n :int):
    if n==0:
        return 1
    else:
        return n*pactorial(n-1)
    

print(pactorial(N))