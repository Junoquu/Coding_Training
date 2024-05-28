n=int(input())

for _ in range(n):
    string=input()
    if string[-1]!='.':
        print(string+'.')
    else:
        print(string)