import sys

def mode(list):
    dic=dict()
    for i in list:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    mx=max(dic.values())
    mx_dic=[]

    for i in dic:
        if mx==dic[i]:
            mx_dic.append(i)

    if len(mx_dic)>1:
        return mx_dic[1]
    else:
        return mx_dic[0]

n=int(sys.stdin.readline())
n_list=[]

avg=0
mid=0
many=0
num_len=0

for i in range(n):
    n_list.append(int(sys.stdin.readline()))

sorted_list=sorted(n_list)

avg=sum(sorted_list)/n
mid=sorted_list[(len(sorted_list)//2)]
many=mode(sorted_list)
num_len=max(sorted_list)-min(sorted_list)

print(round(avg))
print(mid)
print(many)
print(num_len)