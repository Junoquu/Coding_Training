n=int(input())
scores=[]

for _ in range(n):
    a,d,g=map(int,input().split())

    if a!=(d+g):
        scores.append(a*(d+g))
    else:
        scores.append(2*a*(d+g))
print(max(scores))