def solution(order):
    answer = 0
    
    amer_order = ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    latte_order = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte"]
    
    for coffee in order:
        if coffee in amer_order:
            answer += 4500
        elif coffee in latte_order:
            answer += 5000
    
    return answer