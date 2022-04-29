# 01 유효한 팰린드롬

[리트코드 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

난이도 ★

## 풀이

> 64ms, 14.6MB
> 
- 리스트 컴프리헨션을 사용하여 s에서 알파벳과 숫자만 합친 후 소문자로 변환
- 슬라이싱을 사용하여 해당 문자열이 뒤집은 문자열과 같으면 return True, 다르면 return False

```python
# 처음에 이렇게 했는데 계속 true만 나옴..
def isPalindrome(self, s: str) -> bool:
    s = ''.join(a for a in s if a.isalnum()).lower()
    if s == s[::-1]:
        answer = 'true'
    else:
        answer = 'false'
    return answer

# 이렇게 바꿨더니 제대로 출력됨
def isPalindrome(self, s: str) -> bool:
    s = ''.join(a for a in s if a.isalnum()).lower()
    if s == s[::-1]:
        return True
    else:
        return False
```

## 학습해야할 부분

`isalnum()` 영문자, 숫자 여부를 판별하는 함수

`lower()` 모두 소문자로 변환

`s[::-1]` 문자열 뒤집기

`s[:]` 사본 리턴. a = b 형태로 할당하면 변수값 할당이 아니라 a 변수가 b 변수를 참조하는 형태. 참조가 아닌 값을 복사하기 위해 [:] 사용

## 가능한 풀이

1. 리스트로 변환 (304ms)
    
    `pop()` 함수에서 인덱스를 지정하여 맨 뒷부분의 `pop()` 결과와 매칭
    
    일치하지 않는 경우 `return False`, 모두 통과했다면 `return True`
    
    ```python
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
    	    if char.isalnum():
                strs.append(char.lower())
    
    	# 팰린드롬 여부 판별
    	while len(strs) > 1:
    		if strs.pop(0) != strs.pop():
    			return False
    		
    	return True
    ```
    
2. 데크 자료형을 이용한 최적화 (64ms)
    
    리스트의 `pop(0)`은 $O(n)$, 데크의 `popleft()`는 $O(1)$
    
    ```python
    def isPalindrome(self, s: str) -> bool:
    	# 자료형 데크로 선언
        strs: Deque = collections.deque()
    
        for char in s:
    		if char.isalnum():
    			strs.append(char.lower())
    
    	while len(strs) > 1:
    		if strs.popleft() != strs.pop():
    			return False
    		
    	return True
    ```
    
3. 슬라이싱 사용 (36ms)
    
    정규식으로 불필요한 문자 필터링, 슬라이싱으로 문자열 조작
    
    문자열 조작시 슬라이싱을 사용하는 편이 속도 개선에 유리
    
    ```python
    def isPalindrome(self, s: str) -> bool:
    	s = s.lower()
    	# 정규식으로 불필요한 문자 필터링
    	s = re.sub('[^a-z0-9]', '', s)
    
    	return s == s[::-1] # 슬라이싱
    ```
    
4. C 구현 (4ms)
    
    문자열을 저장하는 char 포인터에 대한 직접 조작
