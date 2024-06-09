emoji=input()

colons=0
under_bar=0

for i in emoji:
    if i==':':
        colons+=1
    elif i=='_':
        under_bar+=1
difficult=(len(emoji))+colons+under_bar*5
print(difficult)