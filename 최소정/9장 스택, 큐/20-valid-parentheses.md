# 20 유효한 괄호

[리트코드 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

난이도 ★

## 풀이

> 48ms, 13.9MB
> 
- for문에 괄호 유효 케이스를 다 넣었더니 지저분해져서 딕셔너리로 먼저 정리함
- 왼쪽 괄호를 key로, 오른쪽 괄호를 value로
- 왼쪽 괄호인 경우 stack에 push하고 stack의 마지막 요소를 key로 한 value가 입력값과 일치할 경우 pop
- 그 외의 경우와 stack에 요소가 없는데 오른쪽 괄호가 들어온 경우 False
- for문이 끝나고 stack에 남은 값이 없는 경우 True

```python
def isValid(self, s: str) -> bool:
    stack = []
    prnth = {'(': ')', '{': '}', '[': ']'}
    
    for p in s:
        if not stack and p not in prnth:
            return False
        elif p in prnth:
            stack.append(p)
        elif prnth[stack[-1]]==p:
            stack.pop()
        else:
            return False
    
    if not stack:
        return True
    # return len(stack) == 0
```

## 가능한 풀이

1. 스택 일치 여부 판별
    - (, [, {는 스택에 푸시하고, ), ], }를 만날 때 스택에서 팝한 결과가 매핑 테이블 결과와 매칭되는지 확인
    - 먼저 매핑 테이블을 만들고 테이블에 존재하지 않으면 무조건 푸시, 팝했을 때 결과가 일치하지 않으면 False 리턴
    - 예외 처리! → 팝 결과가 일치하지 않는지 확인하는 것 외에도 스택이 비어있는 지 여부 확인 필요
    
    ```python
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
    ```
    
    
