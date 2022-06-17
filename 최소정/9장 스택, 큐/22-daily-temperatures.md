# 22 일일 온도

[리트코드 739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

난이도 ★★

## 풀이

> Time Limit Exceeded :)
> 
- 만약 현재 온도가 이후 온도 중 최댓값이라면 0일 append 하도록 함
- 현재보다 높은 온도가 나올 때까지 스택에 계속 쌓고, 높은 온도가 나오면 현재 스택의 길이를 append하고 스택을 비움

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack, answer = [], []
    
    for i in range(len(temperatures)): 
        stack.append(temperatures[i])
        if stack[0] == max(temperatures[i:]):
            answer.append(0)
            stack.pop()
            continue
        
        while temperatures[i+1] <= stack[0]:
            stack.append(temperatures[i+1])
            i += 1
            
        answer.append(len(stack))
        stack.clear()
    
    return answer
```

## 가능한 풀이

- 현재의 인덱스를 계속 스택에 쌓아두다가 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이 비교
- 더 높다면 스택의 값을 팝으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리
- 더 높은 온도가 나오지 않아 스택에서 비워지지 않으면 해당 인덱스는 0으로 남게 됨 (디폴트 값이 0이므로)

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures) # 디폴트 값 0
    stack = []
    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop() # 처리한 인덱스 스택에서 제거
            answer[last] = i - last # 현재 인덱스와 쌓아둔 인덱스의 차이
        stack.append(i)
    
    return answer
```

## 학습할 부분

- `enumerate()`를 잘 활용해보자!!
