n = int(input())

people = []

for _ in range(n):
    info = input().split()
    people.append((int(info[0]),info[1]))
    
people = sorted(people, key = lambda x :x[0] )

for i in people:
    print(*i)