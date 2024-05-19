string=input()
result=''
result+=string[0]
for i in range(1,len(string)):
    
    if string[i]==string[i-1]:
        continue
    result+=string[i]
print(result)