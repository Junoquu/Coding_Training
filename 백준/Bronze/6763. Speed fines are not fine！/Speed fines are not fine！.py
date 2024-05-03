limit = int(input())
speed = int(input())
excess_speed = speed-limit
fine=0

if excess_speed>=1 and excess_speed<=20:
    fine=100
elif excess_speed>=21 and excess_speed<=30:
    fine=270
elif excess_speed>30:
    fine=500
if fine==0:
    print('Congratulations, you are within the speed limit!')
else:
    print(f'You are speeding and your fine is ${fine}.')