def memo_fuc(n,memo):
    if n<2:
        return 1
    if memo[n]!=0:
        return memo[n]
    memo[n]=n*memo_fuc(n-1,memo)
    return memo[n]

n=int(input())
memo=[0]*21

print(memo_fuc(n,memo))