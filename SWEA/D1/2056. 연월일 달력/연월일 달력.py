def check_day(month,day):
    m=int(month)
    d=int(day)
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d>=1 and d<=31:
            return True
    elif m==4 or m==6 or m== 9 or m==11:
        if d>=1 and d<=30:
            return True
    elif m==2:
        if d>=1 and d<=28:
            return True
    else:
        return False

t=int(input())

for tc in range(t):
    date=input()
    year=date[:4]
    month=date[4:6]
    day=date[6:]
    if check_day(month,day):
        print(f"#{tc+1} {year}/{month}/{day}")
    else:
        print(f"#{tc+1} -1 ")