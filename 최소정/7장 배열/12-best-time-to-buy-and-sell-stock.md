# 12 주식을 사고팔기 가장 좋은 시점

[리트코드 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

난이도 ★

## 풀이

> 1579ms, 25.1MB
> 
- 처음에 브루트 포스로 계산했다가 시간 초과가 떠서 다른 방법을 찾음
- 최저 가격을 prices의 0번째 값으로, 최대 이익을 0으로 초기화
- prices를 돌면서 현재 최저 가격과 최대 이익을 계속 업데이트

```python
def maxProfit(self, prices: List[int]) -> int:
    min_price, max_profit = prices[0], 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit
```

## 가능한 풀이

1. 브루트 포스로 계산 (타임아웃)
    - O(n^2)으로 사고팔고를 반복하며 마지막에 최대 이익 산출
    
    ```python
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
                
        return max_price
    ```
    
2. 저점과 현재 값과의 차이 계산 (64ms) → 카데인 알고리즘 응용
    - 현재값을 가리키는 포인터가 우측으로 이동하면서
    - 이전 상태의 저점을 기준으로 가격 차이를 계산하고
    - 만약 클 경우 최댓값을 계속 교체해나가는 형태로 O(n) 풀이
    - 최댓값 변수는 최솟값으로, 최솟값 변수는 최댓값으로 지정
        
        `profit = -sys.maxsize` `min_price = sys.maxsize`
        
    - 단, 이 문제에서는 profit이 최종 결과로 리턴되는데 입력값이 []인 경우, 빈 배열인 경우 `-sys.maxsize`가 그대로 리턴될 수 있으므로 `profit = 0`으로 설정
    - 최저점과 비교해 더 작을 경우 최솟값을 갱신
    - 현재 값과 최솟값과의 차이를 계산해 만약 더 클 경우 최댓값 profit을 계속 갱신하면서 반복
    
    ```python
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit
    ```
    

