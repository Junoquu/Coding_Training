n=int(input())

for i in range(n):
    new_string=''    
    string=input()
    new_string+=string[0]
    for i in string[1:]:
        if i!=new_string[-1]:
            new_string+=i
    print(new_string)