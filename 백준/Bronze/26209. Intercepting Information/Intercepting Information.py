signal=list(map(int,input().split()))

chk=True

for i in signal:
    if i==0 or i==1:
        continue
    else:
        chk=False
        break

if chk:
    print('S')
else:
    print('F')