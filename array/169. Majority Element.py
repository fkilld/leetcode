# Question: Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # We will use the Boyer-Moore Voting Algorithm
        # Initialize a variable to store the candidate for majority element
        candidate = None
        # Initialize a counter for the candidate
        count = 0

        # Iterate through each number in the list
        for num in nums:
            # If count is 0, set the current number as the new candidate
            if count == 0:
                candidate = num
                # print("New candidate set:", candidate)
            # If the current number is the candidate, increment the count
            if num == candidate:
                count += 1
                # print("Incremented count for candidate", candidate, "->", count)
            # If the current number is not the candidate, decrement the count
            else:
                count -= 1
                # print("Decremented count for candidate", candidate, "->", count)

        # After the loop, candidate is the majority element
        return candidate

# Detailed Example:
# Input: nums = [2,2,1,1,1,2,2]
# Step-by-step:
# count = 0, candidate = None
# num = 2: count == 0, candidate = 2, count = 1
# num = 2: num == candidate, count = 2
# num = 1: num != candidate, count = 1
# num = 1: num != candidate, count = 0
# num = 1: count == 0, candidate = 1, count = 1
# num = 2: num != candidate, count = 0
# num = 2: count == 0, candidate = 2, count = 1
# Output: 2

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    result = sol.majorityElement(nums)
    print("The majority element is:", result)
    # Output:
    # The majority element is: 2
