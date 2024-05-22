n_list=list(map(int,input().split()))

max_n=max(n_list)
sum_n=0
multi_n=1

for i in n_list:
    if i != max_n:
        sum_n+=i
        multi_n*=i

if max_n==sum_n:
    print(1)
elif max_n==multi_n:
    print(2)
else:
    print(3)