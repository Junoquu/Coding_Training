logo=input()

cnt=0

for i in range(0,len(logo)-3):
    if logo[i:i+4]=='DKSH':
        cnt+=1
print(cnt)