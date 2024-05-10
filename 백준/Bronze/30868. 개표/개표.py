n=int(input())

for i in range(n):
    score=int(input())
    
    if score>4:
        for j in range(score//5):
            print('++++',end=' ')
    if score%5>0 or score<5:
        for j in range(score%5):
            print('|',end='')
    print()