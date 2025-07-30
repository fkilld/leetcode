class Solution(object):
    def removeElement(self, nums, val):
        """
        Removes all instances of 'val' in-place from the list 'nums' and returns the new length.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.
        :type nums: List[int]
        :type val: int
        :rtype: int

        Example:
        nums = [3,2,2,3], val = 3
        After calling removeElement(nums, 3):
        nums[:2] == [2,2], return value is 2
        """

        # Initialize a pointer 'i' to track the position to overwrite with non-'val' elements
        i = 0  # 'i' will count the number of elements not equal to 'val'

        # Iterate through each element in the array
        for j in range(len(nums)):
            # If the current element is not equal to 'val'
            if nums[j] != val:
                # Place it at the current 'i' position (overwrite if needed)
                nums[i] = nums[j]
                # Move the 'i' pointer forward
                i += 1
            # If nums[j] == val, do nothing (skip this element)

        # After the loop, 'i' is the new length of the array without 'val'
        return i

        # Detailed Explanation:
        # - We use two pointers: 'i' (write pointer) and 'j' (read pointer).
        # - For every element not equal to 'val', we copy it to the front of the array at index 'i'.
        # - We increment 'i' only when we write a non-'val' element.
        # - At the end, the first 'i' elements of 'nums' are all the elements except 'val'.
        # - The function returns 'i', the new length of the array after removal.
        # - The elements beyond index 'i' are not guaranteed to be in any order or value.

# Example usage and step-by-step explanation:
if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    sol = Solution()
    k = sol.removeElement(nums, val)
    print("Number of elements after removal:", k)
    print("Array after removing val:", nums[:k])
    # Output:
    # Number of elements after removal: 2
    # Array after removing val: [2, 2]
