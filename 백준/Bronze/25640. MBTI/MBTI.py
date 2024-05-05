mbti=input()
n=int(input())
mbti_list=[]
for i in range(n):
    mbti_list.append(input())
cnt=0
for i in mbti_list:
    if i==mbti:
        cnt+=1
    
print(cnt)