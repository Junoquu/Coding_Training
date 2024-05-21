w1=int(input())
h1=int(input())
w2=int(input())
h2=int(input())

result=(w1+w2)+(max(w1,w2)-min(w1,w2)) + (h1+h2)*2 + 4
print(result)