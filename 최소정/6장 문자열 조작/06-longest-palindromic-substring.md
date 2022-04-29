# 06 가장 긴 팰린드롬 부분 문자열

[리트코드 5. Longest Palindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/)

난이도 ★★

## 풀이

> 229ms, 13.9MB
> 
- 홀수인 경우와 짝수인 경우를 나누어야겠다는 생각은 했지만, 아직은 낯선 투포인터...결국 책봤습니다..담엔 스스로 풀 수 있길!

```python
def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right] # s[left]와 s[right]가 일치하지 않는 경우
                                 # while 문을 벗어나므로 이전 단계의 팰린드롬 리턴해야함
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                        expand(i, i + 1), # 짝수 투 포인터
                        expand(i, i + 2), # 홀수 투 포인터
                        key=len)
    return result
```

## 학습할 부분

- 예외 처리!
    - 파이썬의 문자열 슬라이싱 - 매우 빠르기 때문에 `s == s[::-1]`로 필터링하는 것만으로도 전체적인 풀이 속도 향상에 매우 큰 도움
- 슬라이싱과 인덱스 조회 - 숫자 표기 방식 혼동 주의! 버그의 주범
    
    ```python
    s = '12345'
    
    # 슬라이싱: n-1만큼 출력
    >>> s[1:3] # 인덱스 1~2
    23
    
    # 인덱스 조회: 해당 인덱스의 값
    >>> s[3] # 인덱스 3
    4
    ```
    

## 가능한 풀이

- 다이나믹 프로그래밍: 직관적으로 이해가 어렵고, 실행 속도가 늦음
- **투 포인터가 중앙을 중심으로 확장하는 형태**: 좀 더 직관적, 성능이 좋음
    - 2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 앞으로 전진
    - 윈도우에 들어온 문자열이 팰린드롬인 경우, 멈추고 투 포인터 점점 확장
    - expand()로 정의한 중첩 함수에서 홀수, 짝수 2개의  투 포인터가 팰린드롬 여부를 판별하면서 슬라이딩 윈도우처럼 계속 우측으로 이동
    - 이렇게 판별한 최댓값이 최종 결과
