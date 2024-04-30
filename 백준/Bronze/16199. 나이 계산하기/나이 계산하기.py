b_y, b_m, b_d = map(int, input().split())
d_y, d_m, d_d = map(int, input().split())
man_old = 0
if b_m < d_m:
    man_old = d_y-b_y
elif b_m == d_m:
    if b_d <= d_d:
        man_old = d_y-b_y
    else:
        man_old = d_y-b_y-1
else:
    man_old = d_y-b_y-1
count_old = d_y-b_y+1
year_old = d_y-b_y
print(man_old)
print(count_old)
print(year_old)