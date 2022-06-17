# push(x): 요소 x를 스택에 삽입한다.
# pop(): 스택의 첫 번째 요소를 삭제한다.
# top(): 스택의 첫 번째 요소를 가져온다.
# empty(): 스택이 비어 있는지 여부를 리턴한다.

### code
class MyStack:
    # 큐로 스택 정의
    def __init__(self):
        self.q = collections.deque()
    # append
    def push(self, x: int) -> None:
        self.q.append(x)
    # pop (삭제 O)
    def pop(self) -> int:
        return self.q.pop()
    # top을 리턴만 (삭제 X)
    def top(self) -> int:
        return self.q[-1]
    # 비어있는지 여부
    def empty(self) -> bool:
        return not self.q
      
      
 ### test code
MyStack stack = new MyStack()
stack.push(1)
stack.push(2)

stack.top() #2
stack.pop() #2

stack.empty() #Fasle
