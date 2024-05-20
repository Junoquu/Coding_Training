n,m=map(int,input().split())
misha=[]
image=[]
cnt=0

for i in range(n):
    reverse_pixels=''
    pixels=input()
    for pixel in pixels:
        if pixel=='B':
            reverse_pixels+='W'
        elif pixel=='W':
            reverse_pixels+='B'
    misha.append(reverse_pixels)

input()

for i in range(n):
    image.append(input())

for i in range(n):
    for j in range(m):
        if misha[i][j]!=image[i][j]:
            cnt+=1

print(cnt)