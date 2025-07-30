# Question: Given a sorted unique integer array nums, return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
#   - "a->b" if a != b
#   - "a" if a == b

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Initialize the result list to store the ranges
        res = []
        # Initialize the start pointer for the current range
        i = 0
        # Iterate through the nums array
        while i < len(nums):
            # Set the start of the current range
            start = nums[i]
            # Move j forward as long as the next number is consecutive
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            # If start and end are the same, it's a single number
            if start == nums[j]:
                res.append(str(start))
            else:
                # Otherwise, it's a range from start to nums[j]
                res.append(str(start) + "->" + str(nums[j]))
            # Move i to the next new range
            i = j + 1
        return res

# Detailed Example:
# Input: nums = [0,1,2,4,5,7]
# Step-by-step:
# i=0, start=0, j=0
# nums[1]=1 == nums[0]+1, j=1
# nums[2]=2 == nums[1]+1, j=2
# nums[3]=4 != nums[2]+1, so range is 0->2, res=['0->2']
# i=3, start=4, j=3
# nums[4]=5 == nums[3]+1, j=4
# nums[5]=7 != nums[4]+1, so range is 4->5, res=['0->2','4->5']
# i=5, start=7, j=5
# No more consecutive, so single number 7, res=['0->2','4->5','7']
# Output: ['0->2', '4->5', '7']

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,4,5,7]
    result = sol.summaryRanges(nums)
    print("Summary Ranges:", result)
    # Output:
    # Summary Ranges: ['0->2', '4->5', '7']
