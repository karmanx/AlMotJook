## 7장 배열
# 09 세 수의 합

### code
# 브루트포스
# 중간 중간에 중복된 값을 확인하고, 중복된 값이면 건너뜀

def thrSum_zero(nums):
    result = []
    for i in range(len(nums)-2):
        # 중복된 값 건너 뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k > 0 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))
    return result

  
  
# 투 포인터
# 한 개의 변수는 고정. 두 개의 변수는 투 포인터로 간격을 좁혀가면서 합 계산

def thrSum_zero(nums):
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            summation = nums[i] + nums[left]
            if summation < 0:
                left += 1
            elif summation > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                left += 1
                right -= 1
    return result



### test code
nums = [-1,0,1,2,-1,-4]
thrSum_zero(nums)
