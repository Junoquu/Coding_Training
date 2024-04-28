t_1,e_1,f_1=map(int,input().split())
t_2,e_2,f_2=map(int,input().split())
Max=3*t_1+20*e_1+120*f_1
Mel=3*t_2+20*e_2+120*f_2
if Max<Mel:
    print('Mel')
elif Max==Mel:
    print('Draw')
else:
    print('Max')