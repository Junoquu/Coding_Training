vk,jk=map(int,input().split())
vh,jh=map(int,input().split())
v,d,j=map(int,input().split())
hc=v*d*j
lck=vk*jk
lch=vh*jh

print(hc*lck+hc*lch)