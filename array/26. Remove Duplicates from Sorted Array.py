class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the new length.
        The first k elements of nums will be the unique elements in order.
        :type nums: List[int]
        :rtype: int

        Example:
        nums = [0,0,1,1,1,2,2,3,3,4]
        After calling removeDuplicates(nums):
        nums[:5] == [0,1,2,3,4], return value is 5
        """

        # If the array is empty, return 0 (no unique elements)
        if not nums:
            return 0

        # Initialize a pointer 'i' to track the position of the last unique element
        i = 0  # The first element is always unique

        # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            # If the current element is not equal to the last unique element
            if nums[j] != nums[i]:
                # Move the unique pointer forward
                i += 1
                # Place the new unique element at the next position
                nums[i] = nums[j]
            # If nums[j] == nums[i], it's a duplicate, so do nothing

        # The number of unique elements is i + 1 (since 'i' is index-based)
        return i + 1

# Example usage and step-by-step explanation:
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
    # Output:
    # Number of unique elements: 5
    # Array after removing duplicates: [0, 1, 2, 3, 4]

    # Line-by-line explanation:
    # 1. If nums is empty, return 0.
    # 2. Set i = 0 (first unique element).
    # 3. For each j from 1 to end:
    #    - If nums[j] != nums[i], increment i and set nums[i] = nums[j].
    #    - Otherwise, skip (duplicate).
    # 4. Return i+1 as the count of unique elements.
