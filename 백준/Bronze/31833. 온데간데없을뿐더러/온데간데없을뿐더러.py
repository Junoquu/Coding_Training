n = int(input())
a = input().split()
b = input().split()

X = "".join(a)
Y = "".join(b)

print(min(int(X), int(Y)))