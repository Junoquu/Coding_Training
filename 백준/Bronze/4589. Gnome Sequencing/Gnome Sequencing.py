n=int(input())

print('Gnomes:')

for i in range(n):
    n_list=list(map(int,input().split()))
    
    sorted_n_list=sorted(n_list)
    reverse_n_list=sorted(n_list,reverse=True)

    if sorted_n_list == n_list or reverse_n_list==n_list:
        print('Ordered')
    else:
        print('Unordered')