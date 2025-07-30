class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays nums1 and nums2 into nums1 as one sorted array in-place.
        nums1 has a size of m + n, where the first m elements are valid, and the rest are 0s to be filled.
        nums2 has n elements.
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Modifies nums1 in-place.
        """

        # Initialize three pointers:
        # p1: points to the last valid element in nums1 (index m-1)
        # p2: points to the last element in nums2 (index n-1)
        # p: points to the last position in nums1 (index m+n-1)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge nums2 into nums1 starting from the end
        while p1 >= 0 and p2 >= 0:
            # Compare the elements at p1 and p2
            if nums1[p1] > nums2[p2]:
                # If nums1[p1] is greater, place it at the end of nums1
                nums1[p] = nums1[p1]
                p1 -= 1  # Move p1 to the left
            else:
                # If nums2[p2] is greater or equal, place it at the end of nums1
                nums1[p] = nums2[p2]
                p2 -= 1  # Move p2 to the left
            p -= 1  # Move p to the left

        # If there are remaining elements in nums2, copy them
        # (If nums1 is exhausted before nums2)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        # No need to copy the rest of nums1, as they are already in place

# Detailed Example:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Initial pointers: p1=2 (nums1[2]=3), p2=2 (nums2[2]=6), p=5
# Step 1: nums1[2]=3 < nums2[2]=6 -> nums1[5]=6, p2=1, p=4
# Step 2: nums1[2]=3 < nums2[1]=5 -> nums1[4]=5, p2=0, p=3
# Step 3: nums1[2]=3 > nums2[0]=2 -> nums1[3]=3, p1=1, p=2
# Step 4: nums1[1]=2 == nums2[0]=2 -> nums1[2]=2, p2=-1, p=1
# Now, p2 < 0, so done.
# Final nums1: [1,2,2,3,5,6]

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print("Before merge:")
    print("nums1:", nums1)
    print("nums2:", nums2)
    sol.merge(nums1, m, nums2, n)
    print("After merge:")
    print("nums1:", nums1)
    # Output:
    # Before merge:
    # nums1: [1, 2, 3, 0, 0, 0]
    # nums2: [2, 5, 6]
    # After merge:
    # nums1: [1, 2, 2, 3, 5, 6]
