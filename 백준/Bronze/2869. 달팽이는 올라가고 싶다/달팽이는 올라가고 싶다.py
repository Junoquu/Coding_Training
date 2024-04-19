a,b,v = map(int,input().split())
snail=(v-b)//(a-b)
if (v-b)%(a-b)==0:
    print(snail)
else:
    print(snail+1)