start=input().split(' : ')
end=input().split(' : ')
start_sec=3600*int(start[0])+60*int(start[1])+int(start[-1])
end_sec=3600*int(end[0])+60*int(end[1])+int(end[-1])

if end_sec<start_sec:
    end_sec+=86400
print(end_sec-start_sec)