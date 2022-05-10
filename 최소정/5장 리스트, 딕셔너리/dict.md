# 딕셔너리

키/값 구조의 데이터를 저장하는 자료형

내부적으로는 해시 테이블로 구현

파이썬의 해싱 - 숫자, 문자, 집합 등 불변 객체 모두 키로 사용 가능. 해시 테이블을 이용해 자료 저장

해시테이블은 다양한 타입을 키로 지원하면서 입력과 조회 모두 $O(1)$ 가능

최악의 경우 $O(n)$이지만, 분할 상환 분석에 따른 시간 복잡도는 $O(1)$

시간 복잡도 $O(1)$ - `len(a)` `a[key]` `a[key] = value` `key in a`

- 파이썬 3.7+: 딕셔너리 입력 순서 유지
- 파이썬 3.6+: 딕셔너리 메모리 사용량 20% 감소

딕셔너리의 입력 순서가 유지될 것이라 가정하고 진행하는 것은 매우 위험!

## 딕셔너리의 활용 방법

```python
# 딕셔너리 선언
a = dict()
a = {}

# 초기값 지정 선언 및 값 할당
a = {'key1':'value1', 'key2':'value2'}
a['key3'] = 'value3'

# KeyError - 존재하지 않는 키 조회/삭제시 발생
# try 구문으로 예외 처리 -> 나중에 삽입하는 등 별도 추가 작업 가능
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# 키가 존재하는지 미리 확인
'key4' in a
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

# items() 메소드로 키/값 조회
for k,v in a.items():
		print(k,v)

# del로 키 삭제
del a['key1']
```

## 딕셔너리 모듈

- **defaultdict 객체**
    
    존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 
    
    디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템 생성
    
    ```python
    # 실제로는 collections.defaultdict 클래스를 가짐
    # A와 B에 5와 4 할당 -> 2개의 아이템 존재
    a = collections.defaultdict(int)
    a['A'] = 5
    a['B'] = 4
    a
    -----------
    defaultdict(<class 'int'>, {'A': 5, 'B': 4})
    
    # C는 존재하지 않는 키이므로 원래라면 KeyError 발생
    # default 객체는 에러 없이 바로 +1 연산 가능
    # 디폴트인 0을 기준으로 자동 생성한 후 1을 더함
    a['C'] += 1
    a
    -----------
    defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
    ```
    
- **Counter 객체**
    
    아이템에 대한 개수를 계산해 딕셔너리로 리턴
    
    ```python
    # 키 - 아이템 값, 값 - 해당 아이템의 개수
    a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
    b = collections.Counter(a)
    b
    -----------
    Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
    
    # 실제로는 딕셔너리를 한 번 더 래핑한 
    # collections.Counter 클래스를 가짐
    type(b)
    -----------
    <class 'collections.Counter'>
    
    # 가장 빈도수가 높은 요소 추출
    b.most_common(2) # 가장 빈도가 높은 2개 요소 추출
    -----------
    [(5, 3), (6, 2)]
    ```
    
- **OrderedDict 객체**
    
    파이썬 3.6 이하: 해시 테이블을 이용한 자료형의 입력 순서 유지X
    
    OrderedDict는 입력 그대로 순서 유지
    
    ```python
    >>> collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
    OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
    ```
    
    파이썬 3.7+: 딕셔너리 내부적으로 인덱스를 이용하여 입력 순서 유지
    
    하위 버전의 파이썬 인터프리터를 사용할 수도 있으며, 원래 해시 테이블은 입력 순서에 관여하지 않는 자료형인만큼 입력 순서 기대X
    

> **타입 선언**
> 
> 
> ```python
> # 이름으로 선언
> >>> a = list()
> >>> type(a)
> <class 'list'>
> 
> # 기호로 썬언
> >>> type([])
> <class 'list'>
> >>> type(())
> <class 'tuple'>
> >>> type({})
> <class 'dict'>
> >>> type({1}) # 키 없이 값만 선언 -> 집합
> <class 'set'>
> ```
>
