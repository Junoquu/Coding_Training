n=int(input())

for _ in range(n):
    ans=''
    n_list=list(input().split(' '))
    ans=n_list[0]
    print(ans[:int(n_list[1])]+ans[int(n_list[2]):])