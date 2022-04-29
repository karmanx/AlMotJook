## 7장 배열
# 10 배열 파티션1

### code
def arr_part(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        result = sum(nums[0::2]) # 0번째 인덱스부터 2의 간격 인덱스들의 요소들을 추출하여 더함 # 짝수번
    else:
        result = sum(nums[1::2]) # 홀수번
    return result

  
### test code
nums = [1,4,3,2]
arr_part(nums) # 4

nums = [1,4,3,2,5]
arr_part(nums) # 6
