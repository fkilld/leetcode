class Solution(object):
    def searchInsert(self, nums, target):
        """
        Given a sorted list of distinct integers 'nums' and a target value 'target',
        return the index if the target is found. If not, return the index where it would be
        if it were inserted in order.

        This uses binary search for O(log n) time complexity.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize the left and right pointers for binary search
        left = 0  # Start of the search range
        right = len(nums) - 1  # End of the search range

        # Continue searching while the range is valid
        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            # If the middle element is equal to the target, return its index
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, search the right half
            elif nums[mid] < target:
                left = mid + 1  # Move the left pointer to mid + 1
            # If the middle element is greater than the target, search the left half
            else:
                right = mid - 1  # Move the right pointer to mid - 1

        # If the target is not found, 'left' is the correct insertion index
        return left

# Detailed Explanation:
# - We use binary search to efficiently find the target or its insertion point.
# - 'left' and 'right' define the current search range.
# - On each iteration, we check the middle element:
#     - If it's the target, we return its index.
#     - If it's less than the target, we know the target (if present) must be to the right, so we move 'left' up.
#     - If it's greater, the target must be to the left, so we move 'right' down.
# - If the loop ends without finding the target, 'left' will be at the position where the target should be inserted to maintain sorted order.
