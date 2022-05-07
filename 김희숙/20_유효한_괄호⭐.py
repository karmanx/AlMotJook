## 9장 스택, 큐
# 20 유효한 괄호

# 매핑 테이블 이용 # 처음 알았음

### code
def isValid(s):
  table = {')': '(',
           ']': '[',
           '}': '{'}
  stack = []
  
  for char in s:
    if char not in table:
      stack.append(char)
    elif not stack or table[char] != stack.pop():
      return False
    
  return len(stack) == 0


### test code
s = "()"
isValid(s)

s = "{[]}"
isValid(s)

s = "(]"
isValid(s)
