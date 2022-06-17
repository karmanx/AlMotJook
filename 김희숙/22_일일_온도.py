## 9장 스택, 큐
# 22 일일 온도

### code
def day_temp(t):
    result = []
    count = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] < t[j]:
                count = count + 1
                result.append(count)
                count = 0
                break
            else:
                count = count + 1
                if i == (len(t)-2):
                    result.append(0) # 뒤에서 2번째 원소가 마지막 원소보다 큰 경우
                continue

    result.append(0) # 마지막 원소는 항상 0 return   
    return result


### test code
T = [73,74,75,71,69,72,76,73]
day_temp(T)


### stack, que
def dailyTemperatures(self, T: List[int]) -> List[int]:
    answer = [0] * (len(T))
    stack = []
    
    for i, cur in enumerate(T):
        # 온도가 전보다 높아지면 스택이랑 비교 정답처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        # 온도가 내려갈 땐 스택에 쌓기
        stack.append(i)
    
    return answer
