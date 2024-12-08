import sys
input = sys.stdin.readline

from collections import defaultdict

n,m = map(int,input().split())

poketmon = defaultdict(str)

for i in range(n):
    poketmon[i+1] = input().rstrip()
    
reverse_poketmon = {v: k for k, v in poketmon.items()}

for i in range(m):
    code = input().strip()
    
    if code.isdigit():
        key = int(code)
        print(poketmon.get(key))
    else:
        print(reverse_poketmon.get(code))