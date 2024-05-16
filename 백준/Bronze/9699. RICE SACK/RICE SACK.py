n=int(input())

for i in range(n):
    rice=[]
    rice=list(map(int,input().split()))
    
    print(f"Case #{i+1}: {max(rice)}")