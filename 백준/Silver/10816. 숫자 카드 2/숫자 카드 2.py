from collections import defaultdict

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
finds = list(map(int,input().split()))

card_dict = defaultdict(list)

for i in cards:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1

for i in finds:
    if i in card_dict:
        print(card_dict[i],end=" ")
    else:
        print(0, end=" ")