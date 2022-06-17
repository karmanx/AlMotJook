### code
# https://leetcode.com/problems/design-circular-queue/submissions/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        
    # enQueue(): rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value # rear이 가르키는 자리에 value삽입
            self.p2 = (self.p2 +1) % self.maxlen # 다음 자리로 p2포인터 이동. 길이가 넘어가면 나머지 연산자를 이용하여 한바퀴 돌아서 자리찾음
            return True
        else
            return False
        
    # deQueue(): front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False # 내보낼 것이 없는 상태 ->False
        else:
            self.q[self.p1] = None # 삭제
            self.p1 = (self.p1+1) % self.maxlen
            return True
        

    def Front(self) -> int:
        # p1이 가르키는 맨앞의 요소를 반환
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        

    def Rear(self) -> int:
        # 맨 뒤의 요소를 반환 (p2는 이미 뒤에 삽입될 자리를 가르키고 있기 때문에 p2-1이 맨 뒤의 요소를 가르킴)
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1] 
        

    def isEmpty(self) -> bool:
        # p1,p2가 가르키는 자리가 같고, 그 안의 요소가 존재하지 않는다면 큐는 비어있습니다.
        return self.p1 == self.p2 and self.q[self.p1] is None
        

    def isFull(self) -> bool:
        # p1,p2가 가르키는 자리가 같고, 그 안의 요소가 존재하면 공간이 다 찬 상태
        return self.p1 == self.p2 and self.q[self.p1] is not None
        
