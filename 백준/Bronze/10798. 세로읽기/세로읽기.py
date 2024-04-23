n_list=[]

for i in range(5):
    n_list.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(n_list[j]):
            print(n_list[j][i],end='')