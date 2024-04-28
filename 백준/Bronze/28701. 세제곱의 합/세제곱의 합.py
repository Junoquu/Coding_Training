n=int(input())
n_list=[i for i in range(1,n+1)]

print(sum(n_list))
print(sum(n_list)**2)

triple=0
for i in n_list:
    triple+=i**3

print(triple)