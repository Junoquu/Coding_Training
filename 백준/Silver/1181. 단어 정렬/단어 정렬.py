def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = len(list[len(list)//2])
    left = [x for x in list if len(x)<pivot]
    middle = [x for x in list if len(x)==pivot]
    right = [x for x in list if len(x)>pivot]

    return quick_sort(left)+middle+quick_sort(right)

n=int(input())
string=[]
for i in range(n):
    string.append(input())

dic_sorted=sorted(string)

quick_sorted_string=quick_sort(dic_sorted)
result=[]
for i in quick_sorted_string:
    if i not in result:
        result.append(i)

for i in result:
    print(i)