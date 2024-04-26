n=int(input())
sentence=[]

for i in range(n):
    sentence=input().split()
    print(f"Case #{i+1}: ",end='')
    for j in range(len(sentence)-1,-1,-1):
        print(sentence[j],end=' ')
    print()