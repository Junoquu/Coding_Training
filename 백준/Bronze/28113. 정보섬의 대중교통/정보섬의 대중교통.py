walk_time,bus_remain,subway_remain=map(int,input().split())

if walk_time<=subway_remain:
    if bus_remain==subway_remain:
        print("Anything")
    elif bus_remain>subway_remain:
        print("Subway")
    else:
        print("Bus")
else:
    if bus_remain==subway_remain+walk_time:
        print("Anything")
    elif bus_remain>subway_remain+walk_time:
        print("Subway")
    else:
        print("Bus")