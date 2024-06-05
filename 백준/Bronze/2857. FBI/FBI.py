agent = []
fbi=[]

for i in range(5):
    agent.append(input())

for i in range(len(agent)):
    if 'FBI' in agent[i]:
        fbi.append(i+1)

if len(fbi)==0:
    print('HE GOT AWAY!')
else:
    for i in fbi:
        print(i,end=' ')