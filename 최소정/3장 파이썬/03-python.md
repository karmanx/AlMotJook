# 03. 파이썬 

## 파이썬 문법

### 인덴트

PEP 8에 따른 원칙: 공백 4칸

파이참 커뮤니티 에디션의 Reformat Code: 자동으로 PEP 8 기준에 맞춰줌

### 네이밍 컨벤션

스네이크 케이스 - 소문자 단어를 언더스코어(_)로 구분

✨ PEP 8 및 철학에 따라 스네이크 코딩을 지향하자

### 타입 힌트

동적 타이핑 언어지만 타입 명시적 선언 가능

⇒ 가독성↑ 버그 발생 확률↓

```python
a: str = "1"
b: int = 1

def fn(a: int) -> bool:
    ...
```

✨ 코드를 정리할 때 만이라도 타입을 모두 지정해서 보기좋게 제출해보자

`mypy` 타입 힌트 오류 자동 확인

### 리스트 컴프리헨션

기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

람다 표현식에 `map`이나 `filter`를 섞어서 사용하는 것에 비해 가독성 높음

단, 너무 복잡하게 작성할 경우 오히려 가독성이 떨어지므로 표현식 2개 이하로

```python
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
		    a.append(n * 2)

# 리스트 컴프리헨션
a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
```

```python
a = {}
for key, value in original.items():
    a[key] = value

# 딕셔너리 컴프리헨션
a = {key: value for key, value in original.items()}
```

### 제너레이터

루프의 반복 동작을 제어할 수 있는 루틴 형태

`return` 값을 리턴하고 모든 함수의 동작 종료

`yield` 제너레이터가 여기까지 실행중이던 값을 내보냄. 

중간값을 리턴한 다음 함수는 종료되지 않고 맨 끝에 도달할 때까지 실행

`next()` 다음 값 생성

```python
# 종료 조건이 없으므로 계속해서 값 내보냄
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

get_natural_number() # 제너레이터 리턴

# 100개의 값 생성
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))
```

```python
# 여러 타입의 값을 하나의 함수에서 생성
def generator():
    yield 1
    yield 'string'
    yield True
g = generator()

g # 제너레이터 리턴
next(g) # 1
next(g) # 'string'
next(g) # True
```

### range

`range()` range 클래스를 리턴. for 문에서 사용할 경우 매번 다음 숫자 생성

```python
a = [n for n in range(1000000)]
b = range(1000000)
```

a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재

메모리 점유율 a > b

생성 조건만 정해두고 나중에 필요할 때 생성해서 꺼내 쓸 수 있음

인덱스로 접근 시에는 바로 생성하도록 구현

### enumerate

`enumerate()` 인덱스를 포함한 enumerate 객체로 리턴

```python
# 리스트의 인덱스와 값을 함께 출력하는 방법

# 1
for i in range(len(a)): # 전체 길이를 조회하여 루프를 처리하는 형태 깔끔X
    print(i, a[i]) # 불필요한 a[i] 조회 작업

# 2
i = 0
for v in a: # 값은 깔끔하게 처리함
    print(i, v)
    i += 1 # 인덱스를 위한 변수를 별도로 관리하는 것이 깔끔X

# 3
for i, v in enumerate(a): # 인덱스와 값 모두 한번에 깔끔하게 처리
    print(i, v)
```

### // 나눗셈 연산자

`//` 몫을 구하는 연산자. 동일한 정수형을 결과로 리턴하면서 내림 연산자의 역할

`a // b`는 `int(a / b)`와 동일함

`%` 나머지를 구하는 모듈로 연산자

`divmod()` 몫과 나머지를 동시에 구하는 함수

### print

디버깅을 할 때 가장 자주 쓰는 명령

```python
# 콤마(,)로 구분: 띄어쓰기로 값 구분
print('A1', 'B2')

# sep 파라미터로 구분자 지정
print('A1', 'B2', sep=',') # ,로 값 구분

# end 파라미터를 공백으로 처리해 줄바꿈을 하지 않도록 제한
print('aa', end=' ')
print('bb')

# 리스트는 join()으로 묶어서 출력
a = ['A', 'B']
print(' '.join(a)) # 띄어쓰기로 값 구분
```

```python
idx = 1
fruit = "Apple"

# .format 부여 방식
print('{0}: {1}'.format(idx + 1, fruit))
print('{}: {}'.format(idx + 1, fruit))

# f-string 방식 (python 3.6+)
# 변수를 뒤에 별도로 부여할 필요 없이 인라인으로 삽입 가능
# % 나 .format 보다 간결하고 직관적이며 속도 빠름
print(f'{idx + 1}: {fruit}')
```

### pass

널 연산. 아무것도 하지 않는 기능

인덴트 오류 같은 불필요한 오류를 방지하여

목업 인터페이스부터 구현한 다음에 추후 구현을 진행할 수 있게 함

```python
class MyClass(object):
    def method_a(self):
        pass # 없으면 method_b()에서 IndentationError 발생

    def method_b(self):
        print("Method B")

c = MyClass()
```

### locals

`locals()` 로컬 심볼 테이블 딕셔너리를 가져오는 메소드. 업데이트 가능

로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령 → 디버깅에 큰 도움

로컬 스코프에 제한해 정보를 조회할 수 있기 때문에 클래스의 특정 메소드 내부에서나 함수 내부의 로컬 정보를 조회해 잘못 선언한 부분이 없는지 확인하는 용도로 활용 가능

변수명을 일일이 찾아낼 필요 없이 로컬 스코프에 정의된 모든 변수 출력

`pprint`로 출력하면 보기 좋게 줄바꿈 처리를 해주기 때문에 가독성↑

✨ 이해가 덜 됨..나중에 문제 풀 때 꼭 써보고 완벽히 이해하자!

## 코딩 스타일

✨ 개발은 혼자서만 하는 것이 아니며, 좋은 코드란 모두가 이해할 수 있을 때 더 높은 가치를 발휘한다.

### 변수명과 주석

변수명 - 각각의 의미를 부여하여 스네이크 케이스로 작성

주석 - 간단한 주석을 부여하여 가독성↑. 영어로 주석을 읽고 쓰는 데 익숙해지자

### 리스트 컴프리헨션

문법과 의미를 축약하기 때문에 가독성을 떨어트리지 않도록 주의

역할별로 줄 구분, 표현식은 2개 이하

경우에 따라 모두 풀어쓰는 것이 좋을 수도

### 구글 파이썬 스타일 가이드

- 함수의 기본 값으로 가변 객체를 사용하지 않아야 한다. 대신 불변 객체를 사용한다.

```python
# No - [], {}
def foo(a, b=[]):
    ...
def foo(a, b: Mapping ={}):
    ...

# Yes - None을 명시적으로 할당
def foo(a, b=None):
		if b is None:
		    b = []
def foo(a, b: Optional[sequence] = None):
		if b is None:
				b = []
```

- True, False를 판별할 때는 암시적인 방법을 사용한다.

```python
# Yes
if foo:

# No
if foo != []:
```

- 길이가 없다는 말은 값이 없다는 뜻이며, `not users`로 충분하다.

```python
# Yes
if not users:
		print('no users')

# No
if len(users) == 0:
		print('no users')
```

- 정수를 처리할 때는 비교 대상이 되는 정수값을 직접 비교한다.

```python
# Yes
if foo == 0:
		self.handle_zero()

# No
if foo is not None and not foo:
		self.handle_zero()
```

- 모듈로 연산 결과가 0인 것을 정수로 처리한다.

```python
# Yes
if i % 10 == 0:
    self.handle_multiple_of_ten()

# No
if not i % 10:
    self.handle_multiple_of_ten()
```

- 세미콜론으로 줄을 끝내서는 안 되며, 같은 줄에 두 문장을 쓰지 않는다.
- 최대 줄 길이는 80자

✨ 문제를 풀어낼 -바람직하고도 유일하며- 명확한 방법이 존재할 것이다.
