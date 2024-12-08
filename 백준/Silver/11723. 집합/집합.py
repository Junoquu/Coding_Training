import sys
input = sys.stdin.readline

arr = set()
m = int(input())

for _ in range(m):
    cmds = input().split()
    cmd = cmds[0]
    
    if len(cmds) > 1:
        num = int(cmds[1])
    
    if cmd == "add":
        arr.add(num)
    elif cmd == "remove":
        arr.discard(num)
    elif cmd == "check":
        print(1 if num in arr else 0)
    elif cmd == "toggle":
        if num not in arr:
            arr.add(num)
        else:
            arr.remove(num)
    elif cmd == "all":
        arr = set([i for i in range(1,21)])
    elif cmd == "empty":
        arr = set()