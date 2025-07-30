class Solution(object):
    def twoSum(self, nums, target):
        """
        Hash Map Approach - O(n) time, O(n) space
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create hash map to store value -> index mapping for O(1) lookup
        nums_map = {}
        # First pass: populate the hash map with all values and indices
        for i in range(len(nums)):
            # Store each number as key and its index as value
            nums_map[nums[i]] = i
        for i in range(len(nums)):  # Second pass: check for complement of each number
            # Calculate what number we need to reach target
            complement = target - nums[i]
            # Check if complement exists and not same element
            if complement in nums_map and nums_map[complement] != i:
                # Return indices of current element and its complement
                return [i, nums_map[complement]]
        return []  # Return empty array if no solution found

    def twoSum2(self, nums, target):
        """Brute Force Approach - O(n²) time, O(1) space"""
        for i in range(len(nums)):  # Outer loop: iterate through each element as first number
            # Inner loop: check all elements after current as second number
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:  # Check if current pair sums to target
                    return [i, j]  # Return indices if target sum found
        return []  # Return empty array if no valid pair found

    def twoSum3(self, nums, target):
        """Two Pointer Approach (assumes sorted array) - O(n) time, O(1) space"""
        left, right = 0, len(
            nums) - 1  # Initialize pointers at start and end of array
        while left < right:  # Continue until pointers meet
            if nums[left] + nums[right] == target:  # Check if current pair sums to target
                return [left, right]  # Return indices if target found
            elif nums[left] + nums[right] < target:  # If sum is less than target
                left += 1  # Move left pointer right to increase sum
            else:  # If sum is greater than target
                right -= 1  # Move right pointer left to decrease sum
        return []  # Return empty array if no solution found

    def twoSum4(self, nums, target):
        """Sort + Two Pointer Approach - O(n log n) time, O(1) space"""
        nums.sort()  # Sort array first to enable two-pointer technique
        # Initialize pointers at start and end of sorted array
        left, right = 0, len(nums) - 1
        while left < right:  # Continue until pointers meet
            if nums[left] + nums[right] == target:  # Check if current pair sums to target
                # Return indices if target found (NOTE: indices are from sorted array)
                return [left, right]
            elif nums[left] + nums[right] < target:  # If sum is less than target
                left += 1  # Move left pointer right to increase sum
            else:  # If sum is greater than target
                right -= 1  # Move right pointer left to decrease sum
        return []  # Return empty array if no solution found


s = Solution()  # Create instance of Solution class
print(s.twoSum([2, 7, 11, 15], 9))    # Test hash map approach
print(s.twoSum2([2, 7, 11, 15], 9))   # Test brute force approach
# Test two-pointer approach (assumes sorted input)
print(s.twoSum3([2, 7, 11, 15], 9))
print(s.twoSum4([2, 7, 11, 15], 9))   # Test sort + two-pointer approach
