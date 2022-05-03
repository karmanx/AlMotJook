## 8장 연결 리스트
# 13 팰린드롬 연결 리스트

##### 연결리스트는 제대로 공부하고 시작해야겠다. 모르겠음. 문제 이해부터 못했음. 

### code
def isPalindrome(self, head: ListNode) -> bool:
    q : List = []

    if not head:
        return True
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True


### test code
