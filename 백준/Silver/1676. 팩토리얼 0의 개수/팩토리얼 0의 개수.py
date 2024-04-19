n=int(input())
fac=1
zero=0

for i in range(1,n+1):
    fac*=i

while fac%10==0:
    fac//=10
    zero+=1

print(zero)