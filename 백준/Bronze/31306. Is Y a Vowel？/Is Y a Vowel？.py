string=input()

vowel=0
vowel_y=0

for i in string:
    if i in ['a','e','i','o','u']:
        vowel+=1
        vowel_y+=1
    elif i == 'y':
        vowel_y+=1
print(vowel,vowel_y )