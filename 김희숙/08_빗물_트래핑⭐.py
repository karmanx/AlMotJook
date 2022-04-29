## 7장 배열
# 08 빗물 트래핑

### code
# 투 포인터 # 개념 챙기기
def rain_Trap(self, height: List[int]) -> int:
    # height에 값이 없는 경우
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right: # left와 right이 최대 높이 막대에서 만나면 종료
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 더 큰 값을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

### test code
rain = [0,1,0,2,1,0,1,3,2,1,2,1]
rain_Trap(rain) # 6





### 실패한 code
def rain_Trap(lst):
    start_num = 0 
    result = 0
    left = lst[start_num]
    while 1:
        
        for i in range(start_num, len(lst)-2):
            left = lst[start_num]
            #left = max(left, lst[i])
            print("left ",left)
            for j in range(i+2, len(lst)):
                print("j ",j)
                right = lst[j]
                last_j = j
                print("right ", right)
                if left > 0 and right >= left:
                    print("if right ",right)
                    for k in range(start_num,j):
                        result = result + left - lst[k]
                        print("result ",result)
                    break
            break
        start_num = last_j

        if left > 0 and (last_j == len(lst) or last_j == len(lst)-1) :
            break
    
    return result


    # 빗물이 쌓이기 위해서는 right가 left와 같거나 커야함 # right >= left 인 순간 빗물 카운트 가능해짐



rain = [0,1,0,2,1,0,1,3,2,1,2,1]
rain_Trap(rain) # 무한굴레

### 
def rain_Trap(lst):
    start_num = 0 
    result = 0
    left = lst[start_num]
    for i in range(len(lst)):
        left = max(left, lst[i])
        print("left ",left)
        for j in range(i+2, len(lst)):
            print("j ",j)
            right = lst[j]
            print("right ", right)
            if left > 0 and right >= left:
                print("if right ",right)
                for k in range(i,j):
                    result = result + left - lst[k]
                    print("result ",result)
                break
    
    return result


    # 빗물이 쌓이기 위해서는 right가 left와 같거나 커야함 # right >= left 인 순간 빗물 카운트 가능해짐



rain = [0,1,0,2,1,0,1,3,2,1,2,1]
rain_Trap(rain) # 12가 나옴
