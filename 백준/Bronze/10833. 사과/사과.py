n=int(input())
result=0

for i in range(n):
    stu,apple=map(int,input().split())
    result+=apple%stu
print(result)