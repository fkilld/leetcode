# Question: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# In other words, check if the array contains duplicate values such that the indices of the duplicates are at most k apart.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # We will use a dictionary to keep track of the last index where each number was seen.
        last_seen = {}
        # Iterate through the list with both index and value
        for i, num in enumerate(nums):
            # If the number has been seen before
            if num in last_seen:
                # Check if the difference between current index and last seen index is at most k
                if i - last_seen[num] <= k:
                    # Found a duplicate within k distance
                    return True
            # Update the last seen index for the current number
            last_seen[num] = i
        # If no such pair is found, return False
        return False

# Detailed Example:
# Input: nums = [1, 2, 3, 1], k = 3
# Step-by-step:
# last_seen = {}
# i=0, num=1: not in last_seen, set last_seen[1]=0
# i=1, num=2: not in last_seen, set last_seen[2]=1
# i=2, num=3: not in last_seen, set last_seen[3]=2
# i=3, num=1: 1 in last_seen at index 0, i - last_seen[1] = 3 - 0 = 3 <= 3, so return True
# Output: True

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    result = sol.containsNearbyDuplicate(nums, k)
    print("Does the array contain nearby duplicates within k distance?", result)
    # Output:
    # Does the array contain nearby duplicates within k distance? True
