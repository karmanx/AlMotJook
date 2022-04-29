# 03 로그 파일 재정렬

[리트코드 937. Reorder Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)

난이도 ★

## 풀이

```python
letters, digits = [], []

for log in logs:
    if log[-1].isalpha():
        letters.append(log)
    else:
        digits.append(log)

for let in letters:
    let = let.split()

# 여기까지 하다가 책봄..
```

## 학습해야할 부분

- `sort()` 함수: 리스트를 정렬해주는 함수
    
    ```python
    # 기본적으로 오름차순 정렬
    list.sort()
    
    # 내림차순 정렬
    list.sort(reverse=True) # 매개변수 reverse값을 지정
    
    # key: 정렬의 대상이 되는 데이터
    # key 매개변수에 각 요소로부터 key를 만들어낼 수 있도록 정의된 함수 전달
    def getKey(tup):
        return tup[1] # 튜플 첫번째 인덱스 값을 키로 사용
    tups.sort(key=getKey)
    ```
    
- 람다 표현식: 식별자 없이 실행 가능한 함수. 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현
    
    [2개의 키를 람다 표현식으로 정렬하는 문법]
    
    ```python
    s = ['2 A', '1 B', '4 C', '1 A']
    
    # 오름차순 정렬
    sorted(s)
    ---------------
    ['1 A', '1 B', '2 A', '4 C'] # 각 요소의 번호순 정렬
    
    # 그 뒤의 문자순 정렬
    # 문자가 동일한 경우에는 그 앞 번호순 정렬
    def func(x):
        return x.split()[1], x.split()[0]
    
    s.sort(key=func)
    ---------------
    ['1 A', '2 A', '1 B', '4 C']
    
    # 람다 표현식
    s.sort(key=lambda x: x.split()[1], x.split()[0]))
    ---------------
    ['1 A', '2 A', '1 B', '4 C']
    ```
    
    코드가 길어지고 map이나 filter와 함께 섞어서 사용하기 시작하면 가독성 매우 떨어짐
    

## 가능한 풀이

1. 람다와 + 연산자를 이용
    
    ```python
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    ```
    
    - 문자와 숫자를 구분 (로그 자체는 숫자 로그도 모두 문자열로 지정되어 있으므로, 타입을 확인하면 모두 문자로 출력)
        
        ⇒ `isdigit()`으로 숫자 판별
        
    - 문자 로그를 정렬 (식별자를 제외한 문자열 [1:]을 키로 하여 정렬, 동일한 경우 후순위로 식별자 [0]를 지정해 정렬)
        
        ⇒ 람다 표현식 `letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))`
        
    - 문자 로그와 숫자 로그를 이어 붙임
        
        ⇒ + 연산자 `return letters + digits`
