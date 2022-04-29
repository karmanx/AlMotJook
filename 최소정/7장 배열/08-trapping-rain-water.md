# 08 빗물 트래핑

[리트코드 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

난이도 ★★★

## 풀이

책봤다..하하 책보고도 이해가 잘 안돼서 끙끙ㅜㅜ 손으로 직접 돌려보고 이해완!

```python
def trap(self, height: List[int]) -> int:
    # height에 값이 없는 경우
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right: # left와 right이 최대 높이 막대에서 만나면 종료
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
```

## 학습할 부분

- 스터디 전까지 스택 이해해서 들고가기

## 가능한 풀이

> 높이와 너비 모든 공간을 차례대로 살펴보면 O(n^2)이므로 좀 더 효율적인 풀이 찾아야 함
> 
1. 투 포인터를 최대로 이동
    
    ```python
    def trap(self, height: List[int]) -> int:
        # height에 값이 없는 경우
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right: # left와 right이 최대 높이 막대에서 만나면 종료
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    ```
    
    - `if not height`: height에 값이 없는 경우. 길이가 없다는 말은 값이 없다는 말과 같으므로 `len(height) == 0`과 동일
    - 최대 높이의 막대는 전체 부피에 영향을 끼치지 않고 왼쪽과 오른쪽을 가르는 장벽 역할
    - 최대 높이의 막대까지 각각 좌우 기둥 최대 높이와 현재 높이와의 차이만큼 물 높이 volume을 더해 나감
    - 적어도 낮은 쪽은 그만큼 항상 채워질 것이므로, 좌우 어느 쪽이든 낮은 쪽은 높은 쪽을 향해서 포인터가 가운데로 점점 이동
    - 오른쪽이 크다면 `left += 1`로 왼쪽이 이동, 왼쪽이 크다면 `right  -= 1`로 오른쪽이 이동
    - 가장 높이가 높은 막대, ‘최대' 지점에서 좌우 포인터가 서로 만나게 되며 O(n)에 풀이 가능
    
    ![IMG_1233](https://user-images.githubusercontent.com/101550733/163729389-0ac150f7-7a8c-49cc-a1df-5cd7db14ff07.jpg)
    
    - 현재 위치까지의 최대 높이와 현재 높이의 차이를 구하는 것이 핵심!
2. 스택 쌓기
    
    ```python
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                
                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
        return volume
    ```
    
    - 스택에 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때, 꺾이는 부분 변곡점을 기준으로 격차만큼 물 높이 volume을 채움
    - 이전 높이는 고정된 형태가 아니라 들쑥날쑥하기 때문에 계속 스택으로 채워나가다가
    - 변곡점을 만날 때마다 스택에서 하나씩 꺼내면서 이전과의 차이만큼 물 높이 채워 나가기
    - 스택으로 이전 항목들을 되돌아보며 체크하기는 하지만, 기본적으로 한 번만 살펴보기 때문에 O(n)에 풀이 가능
