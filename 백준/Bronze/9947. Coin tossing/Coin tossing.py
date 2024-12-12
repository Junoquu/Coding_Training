while True:
    p1, p2 = input().split()
    
    if p1 == "#" and p2 == "#":
        break
    
    n = int(input())
    
    p1_c, p2_c = 0, 0
    for _ in range(n):
        a, b = input().split()
        
        if a == b:
            p1_c += 1
        else:
            p2_c += 1
            
    print(f"{p1} {p1_c} {p2} {p2_c}")