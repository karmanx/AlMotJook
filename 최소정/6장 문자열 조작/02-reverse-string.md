# 02 문자열 뒤집기

[리트코드 344. Reverse String](https://leetcode.com/problems/reverse-string/)

난이도 ★

## 풀이

> 227ms, 18.3MB
> 

```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

## 학습해야할 부분

`s = s[::-1]` 과 `s[:] = s[::-1]` 의 차이

## 가능한 풀이

1. 투 포인터를 이용한 스왑 (216ms)
    
    투 포인터: 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
    
    문제 조건 ‘리턴 없이 리스트 내부를 직접 조작하라' 
    
    → 점점 더 범위를 좁혀 가며 s 내부를 스왑하는 형태
    
    ```python
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    ```
    
2. 파이썬다운 방식 (208ms)
    
    파이썬의 기본 기능을 이용하면 단 한 줄로 풀이 가능 → 파이썬다운 방식
    
    `reverse()` 함수: 리스트 뒤집음
    
    ```python
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
    ```
    
    ```python
    def reverseString(self, s: List[str]) -> None:
        # s = s[::-1] -> 리트코드에서 오류 발생
        s[:] = s[::-1]
    ```
    
    `s = s[::-1]`은 오류 발생
    
    문제 조건 ‘공간 복잡도를  $O(1)$으로 제한' → 변수 할당 처리에 제약
    
    `s[:] = s[::-1]` 트릭 사용하면 동작함
    
    그러나 이러한 트릭을 사용하려면 각 코딩 테스트 플랫폼에 대한 숙지 필요
