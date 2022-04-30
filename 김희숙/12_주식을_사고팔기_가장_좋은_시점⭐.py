## 7장 배열
# 12 주식을 사고팔기 가장 좋은 시점

### code
def maxProfit(prices):
    lowest = prices[0]
    profit = 0

    for price in prices:
        if price < lowest:
            lowest = price

        if profit < (price - lowest):
            profit = price - lowest

    return profit


## test code
nums = [7,1,5,3,6,4]
maxProfit(nums)
