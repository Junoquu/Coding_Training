def Max(a,b,c):
    max_num=max(a,max(b,c))
    num1=0
    num2=0

    if max_num==a:
        num1,num2=b,c
    elif max_num==b:
        num1,num2=a,c
    elif max_num==c:
        num1,num2=a,b
    return max_num,num1,num2

while True:
    a,b,c = map(int,input().split())
    if a+b+c==0:
        break

    max_num,num1,num2=Max(a,b,c)
    
    if max_num**2==num1**2+num2**2:
        print("right")
    else:
        print("wrong")