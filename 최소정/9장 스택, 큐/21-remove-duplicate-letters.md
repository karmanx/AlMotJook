# 21 중복 문자 제거

[리트코드 316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

난이도 ★★★

## 풀이

> ^^
> 
- 첨엔 중복 문자 제거하고 사전식 순서로 나열하래서 개껌이지 하고 set 썼는데 난이도 별 세개인 걸 보고 뭔가 잘못 생각했음을 직감... 두번째 테스트 케이스를 보니 단순히 사전식으로 나열하는게 아니라 문자열 순서 유지한 상태로 중복 제거하고 사전에서 가장 먼저 찾을 수 있는 문자열을 찾는 거였음...그리고 안풀림..^^

## 가능한 풀이

1. 재귀를 이용한 분리 (52ms)
    - 중복 문자를 제외한 알파벳 순으로 문자열 입력값 모두 정렬
    - 분리 가능 여부 확인 후 접미사 suffix 분리하여 확인
    - 현재 문자를 리턴하는 재귀 호출 구조로 처리하고 분리 기준점이 되는 문자가 이후 등장하면 모두 replace()로 제거
    - 분할 정복과 비슷한 형태로 접미사 suffix의 크기는 점점 줄어들고 더 이상 남지 않을 때 백트래킹되면서 결과 조합
    
    ```python
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
    ```
    
    ![IMG_CBD875E528A7-1](https://user-images.githubusercontent.com/101550733/168490442-de76dd6c-741d-4f46-a884-f3b609186461.jpeg)

    
2. 스택을 이용한 문자 제거 (32ms)
    - 앞에서부터 차례대로 스택에 쌓아 나감
    - 만약 현재 문자 char가 스택에 쌓여 있는 문자(이전 문자보다 앞선 문자)이고, 뒤에다시 붙일 문자가 남아 있다면(카운터가 0 이상이라면) 쌓아둔 걸 꺼내서 없앰
    - seen은 집합 자료형으로 이미 처리된 문자 여부를 확인하고 이미 처리된 경우 스킵
    - in을 이용한 검색 연산은 스택에 존재하지 않는 연산이므로 별도의 집합 자료형에만 사용
    - stack ADT에 정의된 연산만을 사용해 문제 풀이!
    
    ```python
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
    ```
    
    ![IMG_FFF82BACDB9D-1](https://user-images.githubusercontent.com/101550733/168490433-50231dbd-915c-406d-8dd3-6e46ec8e0001.jpeg)

    
    - 스택 자료구조로 한정짓지 않고 파이썬 리스트로 풀이하면 seen 변수 없이도 풀이 가능
        
        ```python
        def removeDuplicateLetters(self, s: str) -> str:
            counter, stack = collections.Counter(s), []
            
            for char in s:
                counter[char] -= 1
                if char in stack:
                    continue
                # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
                while stack and char < stack[-1] and counter[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(char)
            
            return ''.join(stack)
        ```
        
    
