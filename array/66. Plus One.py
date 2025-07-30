class Solution(object):
    def plusOne(self, digits):
        """
        Given a non-empty list of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list.
        :type digits: List[int]
        :rtype: List[int]

        Example:
        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: 123 + 1 = 124

        Input: digits = [9,9,9]
        Output: [1,0,0,0]
        Explanation: 999 + 1 = 1000
        """

        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            # Add one to the current digit
            digits[i] += 1
            # If the digit is less than 10, no carry is needed
            if digits[i] < 10:
                # Return the result immediately
                return digits
            # If the digit becomes 10, set it to 0 and continue to next digit (carry over)
            digits[i] = 0

        # If we have exited the loop, it means all digits were 9 and now are 0
        # We need to add a new most significant digit '1' at the front
        # For example, [9,9,9] -> [0,0,0] -> [1,0,0,0]
        return [1] + digits

# Detailed Example:
# Input: digits = [2, 9, 9]
# Step 1: i = 2, digits[2] = 9 + 1 = 10 -> set digits[2] = 0, carry over
# Step 2: i = 1, digits[1] = 9 + 1 = 10 -> set digits[1] = 0, carry over
# Step 3: i = 0, digits[0] = 2 + 1 = 3 -> digits[0] = 3, no carry, return [3,0,0]
# Output: [3,0,0]

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    # Test case 1
    digits1 = [1,2,3]
    result1 = sol.plusOne(digits1[:])  # Use [:] to avoid modifying the original
    print("Input:", [1,2,3])
    print("Output:", result1)  # Output: [1,2,4]

    # Test case 2
    digits2 = [9,9,9]
    result2 = sol.plusOne(digits2[:])
    print("Input:", [9,9,9])
    print("Output:", result2)  # Output: [1,0,0,0]

    # Test case 3
    digits3 = [2,9,9]
    result3 = sol.plusOne(digits3[:])
    print("Input:", [2,9,9])
    print("Output:", result3)  # Output: [3,0,0]
