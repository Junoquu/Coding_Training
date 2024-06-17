p=int(input())
c=int(input())
score=p*50-c*10
if p>c:
    score+=500
print(score)