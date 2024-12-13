def solution(before, after):
    answer = 0
    
    before_DAT = [0] * 26
    after_DAT = [0] * 26

    if len(before) != len(after):
        answer = 0
    else:
        for i in before:
            before_DAT[ord(i)-97]+=1
        for i in after:
            after_DAT[ord(i)-97]+=1

        for idx in range(26):
            if before_DAT[idx] != after_DAT[idx]:
                answer = 0
                break
            else:
                answer = 1

    return answer