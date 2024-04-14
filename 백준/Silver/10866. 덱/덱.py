from collections import deque
import sys

input = sys.stdin.readline
n = int(input().strip())
dq = deque()

for _ in range(n):
    command = input().split()
    cmd = command[0]

    if cmd == 'push_front':
        dq.appendleft(int(command[1]))
    elif cmd == 'push_back':
        dq.append(int(command[1]))
    elif cmd == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(0 if dq else 1)
    elif cmd == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
