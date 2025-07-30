from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map and nums_map[complement] != i:
                return [i, nums_map[complement]]
        return []
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []    
    
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum2([2,7,11,15], 9))
print(s.twoSum3([2,7,11,15], 9))