c,b,p=map(int,input().split())
cr,br,pr=map(int,input().split())
cnt=0

if c<cr:
    cnt+=max(c,cr)-min(c,cr)
if b<br:
    cnt+=max(b,br)-min(b,br)
if p<pr:
    cnt+=max(p,pr)-min(p,pr)
print(cnt)