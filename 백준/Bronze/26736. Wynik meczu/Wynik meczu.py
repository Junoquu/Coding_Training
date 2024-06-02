string=input()
a=0
b=0

for _ in string:
    if _=='A':
        a+=1
    elif _=='B':
        b+=1
print(f"{a} : {b}")