string=input()
w,b=0,0

for _ in string:
    if _=='B':
        w+=1
    else:
        b+=1
print(w//2+b//2)