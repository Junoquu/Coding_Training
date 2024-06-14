a1,p1=map(int,input().split())
r1,p2=map(int,input().split())

circle=3.141592653589793*r1*r1
if a1/p1>circle/p2:
    print('Slice of pizza')
else:
    print('Whole pizza')