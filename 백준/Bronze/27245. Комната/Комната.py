w=int(input())
l=int(input())
h=int(input())

minnum=min(w,l)
maxnum=max(w,l)

if (minnum>=2*h) and (maxnum<=2*minnum):
    print('good')
else:
    print('bad')