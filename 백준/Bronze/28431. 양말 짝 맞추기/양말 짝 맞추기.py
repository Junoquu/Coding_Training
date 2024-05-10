n_list=[]
socks=[0]*10
for i in range(5):
    n_list.append(int(input()))
for i in n_list:
    socks[i]+=1

for i in range(10):
    if socks[i]%2!=0:
        print(i)