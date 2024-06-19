def right(list,idx):
    return list[(idx+1)%len(list)]

def left(list,idx):
    return list[(idx-1)%len(list)]

def back(list,idx):
    return list[(idx+2)%len(list)]

dirs=['N','E','S','W']
idx=0
dir=''
for i in range(10):
    num=int(input())

    if num==1:
        dir=right(dirs,idx)
    elif num==2:
        dir=back(dirs,idx)
    elif num==3:
        dir=left(dirs,idx)
    
    idx=dirs.index(dir)
print(dir)