# 07 두 수의 합

[리트코드 1. Two Sum](https://leetcode.com/problems/two-sum/)

난이도 ★

## 풀이

> 3857ms, 14.9MB
> 

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

## 학습할 부분

- 3번과 4번 비교
    - 왜 4번은 `i != nums_map[target - num]` 가 없는지?
    - 왜 인덱스를 return 할 때 순서가 반대인지?

## 가능한 풀이

> 매우 쉽지만 최적화할 수 있는 여러 가지 방법이 있어서 코딩 인터뷰 시 높은 빈도로 출제됨
> 
1. 브루트 포스로 계산 (5284ms)
    
    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    ```
    
    - 브루트 포스: 무차별 대입 방식
    - 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인
    - 마지막 요소들까지 모두 차례대로 비교해 가며 정답을 찾을 때까지 계속 진행
    - 풀이 시간 복잡도 $O(n^2)$ → 비효율적인 풀이법
2. in을 이용한 탐색 (864ms)
    
    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums): # enumerate 객체에 nums의 요소와 인덱스 저장
            complement = target - n
        
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
    ```
    
    - 모든 조합을 비교하지 않고 타겟에서 첫 번째 값을 뺀 값 `target - n`이 존재하는지 탐색
    - `return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]`
        
        nums에서의 index를 구해야 하는데, 두 번째 값은 `nums[i + 1:]`의 index이므로 `i+1` 더하기
        
    - in의 시간 복잡도는 O(n), 전체 시간 복잡도는 $O(n^2)$이지만 in 연산 쪽이 브루트 포스보다 훨씬 가볍고 빠름
3. 첫 번째 수를 뺀 결과 키 조회 (48ms)
    
    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
    ```
    
    - 타겟에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있음
    - 두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장
    - 두 번째 수, 즉 타겟에서 첫 번째 수를 뺀 결과를 키로 조회해보면 두 번째 수의 인덱스 즉시 조회
    - `i != nums_map[target - num]` 같은 인덱스를 출력하지 않도록 처리
    - 딕셔너리의 조회는 평균적으로 O(1), 최악의 경우 O(n)이지만, 분할 상환 분석에 따른 시간 복잡도 O(1)
    - 전체 시간 복잡도 O(n)으로 시간 복잡도 개선
4. 조회 구조 개선 (44ms)
    
    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
    ```
    
    - 딕셔너리 저장과 조회를 2개의 for문으로 각각 처리 → 하나의 for로 합쳐서 처리
    - 전체를 모두 저장할 필요 없이 정답을 찾게 되면 함수를 바로 빠져나옴
    - 그러나 두 번째 값을 찾기 위해 매번 비교하기 때문에 3에 비해 성능상 큰 차이는 없음
    - 코드는 한결 더 간결함
5. 투 포인터 이용 (풀이 불가)
    
    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
    ```
    
    - 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정
    - 코드가 간결하고 이해하기 쉬우며 시간 복잡도가 O(n)
    - But 이 문제는 투 포인터로 풀 수 없음. nums가 정렬된 상태가 아니기 때문에!
        
        → 정렬 로직을 추가해도 인덱스가 엉망이 되기 때문에 불가함
        
    - 인덱스가 아니라 값을 찾아내는 문제는 정렬 후 투 포인터로 풀이 가능하지만, 인덱스를 찾아내는 문제에서는 정렬을 통해 인덱스를 섞으면 안됨
6. 고(Go) 구현 (8ms)
    - 파이썬과 코드는 비슷하지만 좀 더 최적화된 언어를 선택하는 것만으로 6배 빨라짐
    - 언어에 따라 타임아웃이 발생하거나 파이썬은 풀리지 않지만 C나 Go에서 풀리는 경우도 간간이 있음
