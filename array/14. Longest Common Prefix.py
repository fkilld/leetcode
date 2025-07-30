class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    # 1. Horizontal Scanning
    # Time Complexity: O(S), where S is the sum of all characters in all strings.
    # Space Complexity: O(1). We only used constant extra space.

    def longestCommonPrefix(self, strs):
        if not strs:  # Check if input list is empty
            return ""  # Return empty string for empty input
        # Initialize prefix with first string (assume it's the common prefix)
        prefix = strs[0]
        for i in range(1, len(strs)):  # Iterate through remaining strings starting from index 1
            # While current string doesn't start with current prefix
            while strs[i].find(prefix) != 0:
                # Remove last character from prefix to make it shorter
                prefix = prefix[:-1]
                # If prefix becomes empty (no common prefix exists)
                if not prefix:
                    return ""  # Return empty string immediately
        return prefix  # Return the longest common prefix found

    # 2. Vertical Scanning
    # Time Complexity: O(S), where S is the sum of all characters in all strings.
    # Space Complexity: O(1). We only used constant extra space.
    def longestCommonPrefix2(self, strs):
        if not strs:  # Check if input list is empty
            return ""  # Return empty string for empty input
        # Iterate through each character position in first string
        for i in range(len(strs[0])):
            # Get character at current position from first string
            char = strs[0][i]
            for j in range(1, len(strs)):  # Check this character position in all other strings
                # If string is shorter or character doesn't match
                if i == len(strs[j]) or strs[j][i] != char:
                    # Return prefix up to current position (excluding current char)
                    return strs[0][:i]
        # If we've checked all characters, first string is the common prefix
        return strs[0]

        # 3. Divide and Conquer
    # Time Complexity: O(S), where S is the sum of all characters in all strings.
    # Space Complexity: O(m⋅log⁡n), where m is the length of the longest string.
    def longestCommonPrefix3(self, strs):
        if not strs:  # Check if input list is empty
            return ""  # Return empty string for empty input
        # Start divide and conquer with full range
        return self.longestCommonPrefix3(strs, 0, len(strs) - 1)

    # Recursive helper function with left and right boundaries
    def longestCommonPrefix3(self, strs, l, r):
        if l == r:  # Base case: when we have only one string
            return strs[l]  # Return that single string as the prefix
        mid = (l + r) // 2  # Find middle point to divide the array
        # Recursively find LCP for left half
        left = self.longestCommonPrefix3(strs, l, mid)
        # Recursively find LCP for right half
        right = self.longestCommonPrefix3(strs, mid + 1, r)
        # Merge: find common prefix between left and right results
        return self.commonPrefix(left, right)

    # Helper function to find common prefix between two strings
    def commonPrefix(self, left, right):
        # Get minimum length to avoid index out of bounds
        min_len = min(len(left), len(right))
        for i in range(min_len):  # Compare characters up to minimum length
            if left[i] != right[i]:  # If characters don't match at position i
                # Return prefix up to position i (excluding mismatched character)
                return left[:i]
        # If all compared characters match, return the shorter string
        return left[:min_len]

        # 4. Binary Search
    # Time Complexity: O(S⋅log⁡n), where S is the sum of all characters in all strings.
    # Space Complexity: O(1). We only used constant extra space.
    def longestCommonPrefix4(self, strs):
        """
        Binary Search Approach to find the longest common prefix among a list of strings.
        We use binary search on the length of the prefix, checking at each step if all strings
        share a common prefix of a given length.
        Time Complexity: O(S * log n), where S is the sum of all characters in all strings.
        Space Complexity: O(1).
        """
        if not strs:
            return ""  # Return empty string if input list is empty

        # Find the minimum string length in the list, since the common prefix cannot be longer than this
        min_len = min(len(s) for s in strs)

        # Initialize binary search bounds
        low, high = 0, min_len

        # Binary search for the maximum prefix length
        while low <= high:
            mid = (low + high) // 2
            # Check if all strings have the same prefix of length 'mid'
            if self.isCommonPrefix(strs, mid):
                # If yes, try to find a longer prefix
                low = mid + 1
            else:
                # If not, try to find a shorter prefix
                high = mid - 1

        # After the loop, 'high' is the length of the longest common prefix
        return strs[0][:high]

    def isCommonPrefix(self, strs, length):
        """
        Helper function to check if all strings in the list share the same prefix of given length.
        Returns True if they do, False otherwise.
        """
        prefix = strs[0][:length]  # Take the prefix of the first string
        for s in strs[1:]:
            if not s.startswith(prefix):  # If any string does not start with the prefix
                return False
        return True


s = Solution()  # Create instance of Solution class
# Test horizontal scanning approach
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
# Test vertical scanning approach
print(s.longestCommonPrefix2(["flower", "flow", "flight"]))
# Test divide and conquer approach
print(s.longestCommonPrefix3(["flower", "flow", "flight"], 0, 2))
# Test binary search approach
print(s.longestCommonPrefix4(["flower", "flow", "flight"]))
