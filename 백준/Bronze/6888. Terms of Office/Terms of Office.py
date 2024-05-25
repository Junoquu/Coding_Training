def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a*b//gcd(a,b)

change=lcm(4,lcm(2,lcm(3,5)))

start=int(input())
end=int(input())
cnt=1
print(f'All positions change in year {start}')
while True:
    if start+(change*cnt) <= end:
        print(f'All positions change in year {start+(change*(cnt))}')
        cnt+=1
    else:
        break