while True:
    letters = input().split()
    
    if '*' in letters:
        break
    
    test = set()
    
    for str in letters:
        test.add(str[0].upper())
        
    if len(test) > 1:
        print("N")
    else:
        print("Y")