stamp=int(input())
price=int(input())
payment=[0]

if stamp>=5:
    payment.append(500)
if stamp>=10:
    payment.append(price//10)
if stamp>=15:
    payment.append(2000)
if stamp>=20:
    payment.append(price//4)
result=price-max(payment)
if result<0:
    result=0
print(result)