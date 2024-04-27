n=int(input())
n_list=[]
find=False

for i in range(n):
    n_list.append(input())

for i in range(n):
    for j in range(i,n):
        if n_list[i] == n_list[j][::-1]:
            print(len(n_list[i]),n_list[i][len(n_list[i])//2])
            find=True
            break
    if find:
        break