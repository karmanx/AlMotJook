## 7장 배열
# 11 자신을 제외한 배열의 곱

### code
def arr_mul(nums):
    # 가장 빠른 방법은 모든 원소 곱하고 자신을 나누는 것
    # 하지만 문제에서 이를 금지함

    # 집중력 집나감
    result = []
    result2 = []
    r = 1
    l = 1
    
    for i in range(0, len(nums)): # 오른쪽으로 하나씩 곱해보자
        result.append(r)
        r = r * nums[i]
        #print("1", result)

    for i in range(len(nums)-1, -1, -1): # 왼쪽으로 하나씩 곱해보자
        result[i] = result[i] * l
        l = l * nums[i]
        #print("2", result)
  
    return result 


## test code
nums = [1,2,3,4]
arr_mul(nums) #[24,12,8,6]
