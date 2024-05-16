def ceil_num(num):
    if num>int(num):
        return int(num)+1
    else:
        return int(num)

l,w,s=map(int,input().split())

r=ceil_num(l/s)
c=ceil_num(w/s)
print(r*c)