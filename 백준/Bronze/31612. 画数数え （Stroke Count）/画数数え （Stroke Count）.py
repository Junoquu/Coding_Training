stroke_cnt={'j':2,
            'o':1,
            'i':2}
n=int(input())
s=input()
result=0

for i in s:
    result+=stroke_cnt[i]
print(result)