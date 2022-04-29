## 7장 배열
# 07 두 수의 합

### code
def twoSum_index(nums, target):
    idx = []
    for i in range(len(nums)): # 두 수의 합이니까 for문 2번 돌림
        for j in range(i+1, len(nums)): # 앞에서 확인한 조합은 다시 확인 할 필요 없으니 j = i+1부터 돌림
            if nums[i] + nums[j] == target: # 두 수의 합이 target값 이면
                idx.append(i)
                idx.append(j)
    return idx
  
  
### test code
nums = [2, 7, 11, 15]
target = 9

twoSum_index(nums, target) # [0, 1]
