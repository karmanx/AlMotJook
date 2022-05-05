## 8장 연결 리스트
# 14 두 정렬 리스트의 병합

##### 스탭, 큐 부터 먼저 해볼까 했는데 자료구조 기억 안남... 이론부터 다시 공부 쭈고

### code
def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:
  if (not l1) or (l2 and l1.val >l2.val):
    l1, l2 = l2, l1
  if l1:
    l1.next = self.mergeTwoLists(l1.next, l2)
  return l1
