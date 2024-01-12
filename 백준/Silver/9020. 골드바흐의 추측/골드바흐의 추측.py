import math

def is_prime(N): 
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True
    
N = int(input()) 

for _ in range(N):
    num = int(input())
    
    A = num // 2 
    B = num // 2 
    
    for _ in range(num // 2):
        if is_prime(A) and is_prime(B): 
            print(A, B)
            break
        else: 
            A -= 1
            B += 1
