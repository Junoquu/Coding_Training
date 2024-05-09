n,k=map(int,input().split())
score=list(map(int,input().split()))

for i in score:
    grade=(i*100)//n
    if grade>=0 and grade<=4:
        print(1,end=' ')
    elif grade>4 and grade<=11:
        print(2,end=' ')
    elif grade>11 and grade<=23:
        print(3,end=' ')
    elif grade>23 and grade<=40:
        print(4,end=' ')
    elif grade>40 and grade<=60:
        print(5,end=' ')
    elif grade>60 and grade<=77:
        print(6,end=' ')
    elif grade>77 and grade<=89:
        print(7,end=' ')
    elif grade>89 and grade<=96:
        print(8,end=' ')
    elif grade>96 and grade<=100:
        print(9,end=' ')