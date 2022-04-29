# 05 그룹 애너그램

[리트코드 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

난이도 ★★

## 풀이

> 134ms, 17.1MB
> 
- 딕셔너리로 처리해야겠다는 생각은 했지만 각 단어 key가 `''.join(sorted(word))` value를 갖게 한 다음 해당 딕셔너리의 key와 value를 뒤집으려고 삽질하다가..책봤다..
- anagrams의 value가 list이므로 `append(word)` 해주기 (그냥 = word 했다가 2차 삽질..)

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        
    return list(anagrams.values())
```

## 학습할 부분

### 여러 가지 정렬 방법

- `sorted()` 함수 - 별도 함수
    
    리스트, 숫자, 문자 정렬 가능
    
    문자열을 정렬한 후 다시 문자열로 결합하려면 `join()` 이용
    
    `key=` 옵션을 지정해 정렬을 위한 키 또는 함수 별도 지정 가능
    
    ```python
    # 정렬을 위한 함수로 길이를 구하는 len을 지정한 경우
    # 알파벳 순서가 아니라 길이 순서로 정렬됨
    >>> c = ['ccc', 'aaaa', 'd', 'bb']
    >>> sorted(c, key=len)
    ['d', 'bb', 'ccc', 'aaaa']
    
    # 첫 문자열과 마지막 문자열 순으로 정렬하도록 지정한 경우
    a = ['cde', 'cfc', 'abc']
    
    def fn(s):
        return s[0], s[-1]
    
    print(sorted(a, key=fn))
    -------------------------
    ['abc', 'cfc', 'cde']
    
    # 람다 표현식으로 한 줄로 처리
    >>> a = ['cde', 'cfc', 'abc']
    >>> sorted(a, key=lambda s: (s[0], s[-1]))
    ['abc', 'cfc', 'cde']
    ```
    
- `sort()` 메소드 - 리스트 자료형에서 제공
    
    제자리 정렬: 리스트 자체 정렬
    
    제자리 정렬 알고리즘은 입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간 필요 X, 리턴값 X
    
    정렬 결과를 별도로 리턴하는 `sorted()`와 다름!
    
    ```python
    alist.sort()         # sort()는 리스트 자체를 제자리 정렬
    alist = blist.sort() # 잘못된 구문
                         # sort() 함수는 None을 리턴하므로 주의 필요
    ```
    

## 가능한 풀이

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)   
    return list(anagrams.values())
```

- 정렬하여 비교해서 애너그램 판단
    
    (애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문)
    
- `sorted()`로 문자열 정렬 후 결과를 리스트 형태로 리턴
    
    → 다시 키로 사용하기 위해 `join()`으로 합쳐 이 값을 키로 하는 딕셔너리로 구성
    
- 애너그램끼리는 같은 키를 갖게 되고 각 키의 값에 `append()`하는 형태가 됨. 즉, 정렬한 값을 키로 하여 딕셔너리에 추가
- 존재하지 않는 키를 삽입하려 할 경우 KeyError가 발생하므로 에러가 나지 않도록 항상 디폴트를 생성해주는 defaultdict()로 선언하기
    
    → 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성
