## 6장 문자열 조작
# 02 문자열 뒤집기

### code
def reverse_list(lst):
  result = lst[::-1] # 리트코드에서는 오류
  #result[:] = lst[::-1] # 해결 >> 변수할당 제한 문제
  return result
  
  
 ### test code
List = ["H","a","n","n","a","h"]
reverse_list(List)
