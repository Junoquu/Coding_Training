def solution(binomial):
    answer = 0
    nomial=[i for i in binomial.split() if i]
    if nomial[1] == "+":
        answer = int(nomial[0])+int(nomial[2])
    elif nomial[1] == "-":
        answer = int(nomial[0])-int(nomial[2])
    elif nomial[1] == "*":
        answer = int(nomial[0])*int(nomial[2])
    return answer