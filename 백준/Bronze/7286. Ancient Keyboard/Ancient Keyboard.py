T = int(input())

for tc in range(T):
    n = int(input())

    time_table = {}

    for _ in range(n):
        c, a, b = input().split()
        a, b = int(a), int(b)
        for i in range(a, b):
            time_table[i] = time_table.get(i, 0) + 1

    for _, v in sorted(time_table.items()):
        print(chr(v + 64), end='')
    print()