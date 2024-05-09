white={'K':0,'P':1,'N':3,'B':3,'R':5,'Q':9}
black={'k':0,'p':-1,'n':-3,'b':-3,'r':-5,'q':-9}

chess=[]
score=0

for i in range(8):
    chess.append(input())

for i in chess:
    for j in i:
        if j in white:
            score+=white[j]
        elif j in black:
            score+=black[j]

print(score)