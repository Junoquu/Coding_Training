while True:
    new_string=''
    try:
        string=input()
        for i in string:
            if i=='i':
                new_string+='e'
            elif i=='I':
                new_string+='E'
            elif i=='e':
                new_string+='i'
            elif i=='E':
                new_string+='I'
            else:
                new_string+=i
        print(new_string)
    except:
        break