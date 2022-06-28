def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = result = ListNode(None)
    heap = []
    
    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    # 힙 추출 이후 다음 노드는 다시 저장
    while heap: # 힙에 아무 값도 남지 않을 때까지 반복
        node = heapq.heappop(heap) # 가장 작은 노드의 연결 리스트부터 차례대로 나옴
        idx = node[1]
        result.next = node[2] # 그 값을 결과가 될 노드 result에 하나씩 추가
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next)) # 추출한 연결리스트의 그 다음 노드는 다시 힙에 추가
            
    return root.next
