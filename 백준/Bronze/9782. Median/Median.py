cnt=1
while True:
    n_list=list(map(float,input().split()))
    
    if len(n_list)==1 and n_list[0]==0:
        break
    if len(n_list)%2==0:
        print(f'Case {cnt}: {n_list[len(n_list)//2]:.1f}')
    else:
        print(f'Case {cnt}: {(n_list[len(n_list)//2]+n_list[(len(n_list)//2)+1])/2:.1f}')
    cnt+=1