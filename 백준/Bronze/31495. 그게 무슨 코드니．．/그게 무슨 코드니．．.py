string=input()

if string[0] == string[-1] == '"' and len(string[1:-1]) > 0:
    print(string[1:-1])
else:
    print('CE')