# 11 자신을 제외한 배열의 곱

[리트코드 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

난이도 ★★

## 풀이

> Time Limit Exceeded
> 
- 시간초과..당연함 O(n)에 풀이하라고 했는데 O(n^2)에 풀었음..:)
- 1을 곱해도 결과에 변함이 없으므로 자기 자신을 1로 바꾸고 전체를 곱하게 하였음
- `tmp = nums[:]`로 nums의 사본을 할당해야 nums의 값에 변함이 없음

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    
    for i in range(len(nums)):
        mul = 1
        tmp = nums[:]
        tmp[i] = 1
        for n in tmp:
            mul *= n
        answer.append(mul)
    
    return answer
```

## 가능한 풀이

1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    - ‘나눗셈을 하지 않고 O(n)에 풀이하라’
    - 변수 i가 오른쪽으로 이동하면서 왼쪽부터 곱해서 out에 추가
    - 왼쪽의 곱셈 결과에 오른쪽 마지막 값부터 차례대로 곱하기
    
    ```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
    ```
    
    
