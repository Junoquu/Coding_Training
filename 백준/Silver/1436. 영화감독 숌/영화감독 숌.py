def find_title_num(n):
    cnt=0
    num=666
    while True:
        if '666' in str(num):
            cnt+=1
        if cnt == n:
            return num
        num+=1

n=int(input())
print(find_title_num(n))