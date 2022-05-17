# push(x): 요소 x를 큐에 삽입한다.
# pop(): 큐의 첫 번째 요소를 삭제한다.
# peek(): 큐의 첫 번째 요소를 가져온다.
# empty(): 큐기 비어 있는지 여부를 리턴한다.

### code
class MyQueue:
    # 스택으로 큐 정의
    def __init__(self):
        self.s = []
        self.r = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        self.peek()
        return self.r.pop()

    def peek(self) -> int:
        # output(=r)이 없으면 모두 재입력
        if not self.r:
            while self.s:
                self.r.append(self.s.pop())
        return self.r[-1]

    def empty(self) -> bool:
        return self.s == [] amd self.r == []
      
      
            
### test code
MyQueue queue = new MyQueue()
queue.push(1)
queue.push(2)

queue.peek() #1
queue.pop() #1

queue.empty() #Fasle
