t, m = map(int,input().split())
num = set()
matrix = []
for tc in range(t):
    arr = input().split()
    name = arr[-1]
    activities = arr[:-1]
    
    max_dot = 0
    current_dot = 0
    
    for activity in activities:
        if activity == ".":
            current_dot += 1
            max_dot = max(current_dot,max_dot)
        else:
            current_dot = 0
    
    num.add(max_dot)
    matrix.append(f"{max_dot} {name}")
    
print(len(num))
for _ in matrix:
    print(_)