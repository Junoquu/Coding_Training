n=int(input())
string=input()
hash=0
hashing=0
for i in range(n):
    alpha=ord(string[i])-96
    hash=alpha*(31**i)
    hashing+=hash
print(hashing)