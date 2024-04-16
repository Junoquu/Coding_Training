n=int(input())
string=input()
hash_list=[]
hash=0

memo=[1]*n
for i in range(1,n):
    memo[i]=memo[i-1]*31

for i in range(n):
    alpha=ord(string[i])-96
    hash=alpha*memo[i]
    hash_list.append(hash)

print(sum(hash_list)%1234567891)