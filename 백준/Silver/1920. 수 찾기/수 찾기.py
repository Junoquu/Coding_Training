n=int(input())
n_list=list(map(int,input().split()))
n_list.sort()

m=int(input())
m_list=list(map(int,input().split()))



for target in m_list:
    start,end=0,n-1
    exist=False

    while start <= end:
        mid = (start + end) // 2

        if n_list[mid] == target:
            exist=True
            print(1)
            break

        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if not exist:
        print(0)