first=int(input())

up=False
down=False
same=False
string=[]

for _ in range(3):
    n=int(input())
    if first<n:
        up=True
    else:
        up=False
    if first>n:
        down=True
    else:
        down=False
    if first==n:
        same=True
    else:
        same=False

    if up:
        string.append('Fish Rising')
    elif down:
        string.append('Fish Diving')
    elif same:
        string.append('Fish At Constant Depth')
    first=n

compare_string=[]

for i in string:
    if i not in compare_string:
        compare_string.append(i)

if len(compare_string)==1:
    print(compare_string[0])
else:
    print('No Fish')