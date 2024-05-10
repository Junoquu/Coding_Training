n=int(input())
sec=1

for i in range(2,n+1):
    sec*=i

print(sec//604800)