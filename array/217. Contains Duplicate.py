# Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# In other words, check if the array contains any duplicates.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # We will use a set to keep track of the numbers we have seen so far.
        seen = set()
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                # Print debug info
                # print("Duplicate found:", num)
                return True
            # Otherwise, add the number to the set
            seen.add(num)
            # print("Added", num, "to set. Current set:", seen)
        # If we finish the loop without finding duplicates, return False
        return False

# Detailed Example:
# Input: nums = [1, 2, 3, 1]
# Step-by-step:
# seen = set()
# num = 1: not in seen, add 1 -> seen = {1}
# num = 2: not in seen, add 2 -> seen = {1, 2}
# num = 3: not in seen, add 3 -> seen = {1, 2, 3}
# num = 1: already in seen, return True
# Output: True

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    result = sol.containsDuplicate(nums)
    print("Does the array contain duplicates?", result)
    # Output:
    # Does the array contain duplicates? True
