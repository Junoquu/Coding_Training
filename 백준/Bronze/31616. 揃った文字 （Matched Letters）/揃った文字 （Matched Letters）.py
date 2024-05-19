n=int(input())
string=input()

for i in range(1,len(string)):
    if string[i-1]!=string[i]:
        print('No')
        break
else:
    print('Yes')