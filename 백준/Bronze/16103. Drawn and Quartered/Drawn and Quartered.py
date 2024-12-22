n,k = map(int,input().split())

str = input()

new_str = [str[i:i+(n//4)] for i in range(0,n,n//4)]

if k%3 == 1:
    new_str[1],new_str[2],new_str[3] = new_str[3],new_str[1],new_str[2]

elif k%3 == 2:
    new_str[1],new_str[2],new_str[3] = new_str[2],new_str[3],new_str[1]
    
print("".join(new_str))