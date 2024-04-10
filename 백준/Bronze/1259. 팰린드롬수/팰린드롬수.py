n=''
check=False
while True:
    n=input()

    if n=='0':
        break
        
    middle=len(n)//2

    for i in range(0,middle):
        if n[i]==n[(len(n)-1)-i]:
            check=True
        else:
            check=False
            break
    if check or (len(n)==1 and n!='0'):
        print("yes")
    else:
        print("no")