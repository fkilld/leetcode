class Solution(object):
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        :type nums: List[int]
        :rtype: int
        """
        # Initialize a variable to hold the result
        result = 0
        # Iterate through each number in the list
        for num in nums:
            # XOR the current result with the current number
            # The property of XOR is that a^a = 0 and a^0 = a
            # So, all numbers appearing twice will cancel out to 0, leaving the single number
            result ^= num
        # Return the single number found
        return result

# Detailed Example:
# Input: nums = [4, 1, 2, 1, 2]
# Step-by-step:
# result = 0
# result ^= 4 -> result = 0 ^ 4 = 4
# result ^= 1 -> result = 4 ^ 1 = 5
# result ^= 2 -> result = 5 ^ 2 = 7
# result ^= 1 -> result = 7 ^ 1 = 6
# result ^= 2 -> result = 6 ^ 2 = 4
# All pairs cancel out, only 4 remains.
# Output: 4

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums = [4, 1, 2, 1, 2]
    result = sol.singleNumber(nums)
    print("The single number is:", result)
    # Output:
    # The single number is: 4
