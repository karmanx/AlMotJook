# 23 큐를 이용한 스택 구현

[리트코드 225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

난이도 ★

## 풀이

> 50ms, 13.9MB
> 

```python
class MyStack:
    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

## 가능한 풀이

1. push() 할 때 큐를 이용해 재정렬
    - 문제의 의도: 큐의 FIFO에 해당하는 연산을 사용하여 스택 구현
    - `push()`에서 요소를 삽입한 후 방금 삽입한 요소를 맨 앞에 두는 상태로 전체를 재정렬
    - 요소 삽입 시 시간 복잡도가 O(n)이라 비효율적이긴 하지만 스택을 큐로 구현하는 방법이다!
    
    ```python
    class MyStack:
        def __init__(self):
            self.q = collections.deque()
    
        def push(self, x: int) -> None:
            self.q.append(x)
            # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
            for _ in range(len(self.q) - 1):
                self.q.append(self.q.popleft())
    
        def pop(self) -> int:
            return self.q.popleft()
    
        def top(self) -> int:
            return self.q[0]
    
        def empty(self) -> bool:
            return len(self.q) == 0
    
    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    ```
    

## 학습할 부분

- 큐를 데크로 선언하는 방법 `self.q = collections.deque()`
- 클래스 복습하기
- 이번에 풀 때는 그냥 스택이라고 생각하고 풀었지만..다음 문제는 스택을 이용한 큐 구현이니까 스택에 해당하는 연산만 사용해서 큐를 구현해봐야겠다
