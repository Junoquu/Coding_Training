from collections import deque

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    
    # 1. 초기화
    alis = [[] for _ in range(n+1)] # 인접 리스트
    DAT_list = [0] * (n+1) # index : 노드, value : 진입 차수
    ans = 0
    
    # 2. 노드 정보 저장
    for idx, value in enumerate(arr):
        alis[idx+1].append(value)
        DAT_list[value]+=1
    
    dq = deque()
    # 3. 진입 차수가 0인 노드를 큐에 넣는다.
    for idx in range(1,n+1):
        if DAT_list[idx]==0:
            dq.append(idx)
            ans += 1
    
    # 4. 위상정렬 진행
    while dq:
        node = dq.popleft()
        
        for next in alis[node]:
            # 연결되어 있던 노드의 진입 차수를 하나 감소
            DAT_list[next]-=1
            
            # 새롭게 진입 차수가 0인 노드들을 큐에 푸쉬
            if DAT_list[next]==0:
                dq.append(next)
                ans+=1
    
    print(ans)