res_name = ""

n = int(input())

for i in range(n):
    Player_dict = {}
    max_price = 0
    max_idx=-1

    m = int(input())
    for j in range(m):
        price, name = input().split()
        int_price = int(price)
        Player_dict[j] = {"price":int_price, "name":name}
        if int_price > max_price:
            max_price = int_price
            max_idx=j
    
    print(Player_dict[max_idx]["name"])