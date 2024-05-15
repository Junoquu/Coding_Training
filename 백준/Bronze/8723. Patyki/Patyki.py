def triangle(lengths):
    if lengths[0]==lengths[1] and lengths[1]==lengths[-1]:
        return 2
    else:
        max_length=max(lengths)
        extra_length=0

        for i in lengths:
            if i!=max_length:
                extra_length+=(i**2)
        
        if max_length**2 == extra_length:
            return 1
        else:
            return 0

lengths=list(map(int,input().split()))

print(triangle(lengths))