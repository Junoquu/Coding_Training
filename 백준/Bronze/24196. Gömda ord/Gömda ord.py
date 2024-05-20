s=input()
result=s[0]
idx=ord(s[0])-64
while idx<=len(s)-1:
    result+=s[idx]
    idx+=ord(s[idx])-64
print(result)