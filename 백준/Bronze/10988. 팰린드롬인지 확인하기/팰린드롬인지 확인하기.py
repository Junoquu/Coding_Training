n = input().strip()
is_palindrome = 1

for i in range(len(n) // 2):
    if n[i] != n[-1-i]:
        is_palindrome = 0 
        break

print(is_palindrome)