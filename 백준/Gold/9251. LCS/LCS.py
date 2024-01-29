import sys
input=sys.stdin.readline



string_A=list(input().rstrip())
string_B=list(input().rstrip())


dp=[[0]*(len(string_B)+1) for _ in range(len(string_A)+1)]


for i in range(len(string_A)):
    for j in range(len(string_B)):
        if i==0 or j==0:
            dp[i][j]=0
        if string_A[i]==string_B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    



        
print(dp[len(string_A)-1][len(string_B)-1])
