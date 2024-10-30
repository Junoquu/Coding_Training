def operator(s: str, n: int) -> int:
    if s == "#":
        n = n - 7
    elif s == "@":
        n = n * 3
    elif s == "%":
        n = n + 5
    return n

t = int(input())

for _ in range(t):
    LIST = list(map(str, input().split()))

    res = float(LIST[0])

    if len(LIST) > 2:
        for i in range(1, len(LIST)):
            res = operator(LIST[i], res)
    else:
        res = operator(LIST[1], res)

    print(f'{res:.2f}')