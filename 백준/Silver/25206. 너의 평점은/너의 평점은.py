grade={
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

eval=0
cnt=0

for i in range(20):
    major,score,credit=input().split()
    if credit!='P':
        eval+=(float(score)*grade[credit])
        cnt+=float(score)
    
print(f'{eval/cnt:.6f}')