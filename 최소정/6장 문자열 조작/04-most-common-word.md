# 04 가장 흔한 단어

[리트코드 819. Most Common Word](https://leetcode.com/problems/most-common-word/)

난이도 ★☆

## 풀이

> 54ms, 13.9MB
> 
- paragraph에서 replace 함수를 이용하여 구두점을 공백으로 치환
- 구두점이 제거된 paragraph를 모두 소문자로 바꾸고 split 함수를 이용하여 공백을 기준으로 문자열 나눔
- 리스트 컴프리헨션을 사용하여 paragraph에서 banned가 아닌 단어만 남김
- max 함수를 사용하여 paragraph에서 가장 개수가 많은 단어 리턴.
    
    이때, key 매개변수에 count 함수 넣어주어야 함
    
    그렇지 않으면 코드 값이 가장 큰 단어가 출력됨
    

```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    for sp in string.punctuation:
        paragraph = paragraph.replace(sp, ' ')
    paragraph = paragraph.lower().split()
    paragraph = [i for i in paragraph if i not in banned]
    return max(paragraph, key=paragraph.count)
```

## 학습할 부분

- `remove()`는 가장 처음 만난 값만 제거함
- 좀 더 의미에 맞는 변수명 사용 (words)
- 정규식 `re.sub(r'[^\w]', ' ', paragraph)` - 단어 문자가 아닌 모든 문자를 공백으로 치환
- 단어 목록에서 각 단어의 개수를 처리하는 법
    
    1) 딕셔너리, 2) Counter 객체
    

## 가능한 풀이

```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                if word not in banned]
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]
```

- 데이터 클렌징: 입력값에 대한 전처리 작업
    - 정규식으로 단어 문자가 아닌 모든 문자를 공백으로 치환
        
        `re.sub(r'[^\w]', ' ', paragraph)` ^는 not, \w는 단어 문자
        
    - 대소문자 구분을 하지 않으므로 모두 소문자로 바꾸고 단어 단위로 저장
        
        `.lower().split()`
        
    - 리스트 컴프리헨션의 조건절에는 banned에 포함되지 않은 단어만을 대상으로 함
        
        `if word not in banned`
        
        ⇒ words에 구두점과 banned를 제외한 소문자 단어 목록 저장됨
        
- 각 단어의 개수 처리
    1. 딕셔너리 사용
        
        ```python
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)
        ```
        
        - 개수를 담아두는 변수로 딕셔너리 사용
        - defaultdict()를 사용해 int 기본값이 자동으로 부여되게 함
            
            → 키 존재 유무 확인할 필요 없이 `counts[word] += 1` 수행
            
        - `max()`함수에 key를 지정해 counts에서 값이 가장 큰 키를 가져옴
    2. Counter 객체 사용
        
        ```python
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
        ```
        
        - words에서 가장 흔하게 등장하는 단어의 첫 번째 값
            
            `most_common(1)` → `[(’ball’, 2)]` → `[0][0]` 추출
            
            ⇒ 첫 번째 인덱스의 키를 추출
