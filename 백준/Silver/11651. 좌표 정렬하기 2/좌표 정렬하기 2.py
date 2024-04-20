n=int(input())
matrix=[]
for i in range(n):
    x,y = map(int,input().split())
    matrix.append((x,y))
sorted_matrix = sorted(matrix,key = lambda x:(x[1],x[0]))

for i in sorted_matrix:
    print(i[0],i[1])