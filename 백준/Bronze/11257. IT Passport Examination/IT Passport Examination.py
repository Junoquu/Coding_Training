n=int(input())

strategy=35*0.3
mangement=25*0.3
skill=40*0.3

for i in range(n):
    num,a,b,c=map(int,input().split())

    if a>=strategy and b>=mangement and c>=skill and a+b+c>=55:
        print(f'{num} {a+b+c} PASS')
    else:
        print(f'{num} {a+b+c} FAIL')