import sys
sys.setrecursionlimit(10**6)

def factorial(n, memo):
    if n<2:
        return 1
    if memo[n]!=0:
        return memo[n]
    return factorial(n-1,memo)*n

n=int(input())
memo=[0]*(n+1)

print(factorial(n,memo))