alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string=input()

for i in alpha:
    if i not in string:
        print(i)
        break