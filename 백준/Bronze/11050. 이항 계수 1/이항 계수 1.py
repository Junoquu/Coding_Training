def fac(n, memo):
    if n < 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = n * fac(n - 1, memo)
    return memo[n]

n,k=map(int,input().split())
n_list=[0]*(n+1)

nCk = fac(n,n_list)//(fac(n-k,n_list)*fac(k,n_list))

print(nCk)