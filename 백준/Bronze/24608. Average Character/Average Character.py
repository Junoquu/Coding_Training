Alphas = input()

idx = 0

for alpha in Alphas:
    idx += ord(alpha)

print(chr(int(idx/len(Alphas))))