import sys

def round_fun(n):
    if n-int(n)>=0.5:
        return int(n)+1
    else:
        return int(n)

n=int(sys.stdin.readline())

if n!=0:
    n_list=[]

    for i in range(n):
        n_list.append(int(sys.stdin.readline()))
    m=round_fun(n*0.15)
    n_list.sort()
    if m>0:
        print(round_fun(sum(n_list[m:-m])/len(n_list[m:-m])))
    else:
        print(round_fun(sum(n_list)/len(n_list)))
else:
    print(0)
