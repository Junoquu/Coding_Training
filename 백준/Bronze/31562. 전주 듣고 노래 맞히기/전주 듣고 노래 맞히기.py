n,m=map(int,input().split())
data=''
music_info=''
music_name=''
music_struc=''

music={}
test=[]

for i in range(n):
    data=input()
    t,music_info=data.split(' ',1)
    music_name,music_struc=music_info.split(' ',1)
    pre_music_struc=music_struc.replace(' ','')
    if music_name not in music:
        music[music_name]=pre_music_struc[:3]

for i in range(m):
    code=input()
    code=code.replace(' ','')
    test.append(code)

for i in test:
    result=[]
    for j in music:
        if i in music[j]:
            result.append(j)
    if len(result)>1:
        print("?")
    elif len(result)==1:
        print(result[0])
    else:
        print("!")