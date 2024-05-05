bun,patty=map(int,input().split())
hambuger=0

if (bun//2)>=patty:
    hambuger=patty
else:
    hambuger=bun//2

print(hambuger)