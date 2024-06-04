alpha={'a':4,'e':3,'i':1, 'o':0, 's':5}
string=input()

for i in string:
    if i in alpha:
        print(alpha[i],end='')
    else:
        print(i,end='')