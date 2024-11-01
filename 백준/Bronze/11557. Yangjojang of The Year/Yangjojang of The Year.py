mt = {}
max_drink=0
max_drink_idx=""

t = int(input())

for _ in range(t):
    n = int(input())

    mt.clear()
    max_drink = 0
    max_drink_idx = ""

    for i in range(n):
        school, drink = input().split()
        drink = int(drink)
        mt[school]=drink
        if max_drink < drink:
            max_drink=drink
            max_drink_idx=school
    print(max_drink_idx)