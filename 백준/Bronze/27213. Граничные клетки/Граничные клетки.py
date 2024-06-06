n=int(input())
m=int(input())

if m>1 and n>1:
    print(n*m-((n-2)*(m-2)))
else:
    print(max(n,m))