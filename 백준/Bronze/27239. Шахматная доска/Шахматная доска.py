alpha={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',0:'h'}
n=int(input())

if n%8>0:
    a=n//8+1
else:
    a=n//8

print(f'{alpha[n%8]}{a}')