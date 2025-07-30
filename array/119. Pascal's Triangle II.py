class Solution(object):
    def getRow(self, rowIndex):
        """
        Returns the rowIndex-th (0-indexed) row of Pascal's Triangle.
        :type rowIndex: int
        :rtype: List[int]
        """
        # Initialize the first row of Pascal's Triangle
        row = [1]
        
        # Build each row up to rowIndex
        for i in range(1, rowIndex + 1):
            # Create a new row with 1s at both ends
            new_row = [1] * (i + 1)
            # Fill in the inner elements of the row
            for j in range(1, i):
                # Each element is the sum of the two elements above it in the previous row
                new_row[j] = row[j - 1] + row[j]
            # Update row to the new_row for the next iteration
            row = new_row
        
        # Return the rowIndex-th row
        return row

# Detailed Example:
# Input: rowIndex = 3
# Step-by-step:
# i=1: new_row = [1, 1]
#      row = [1, 1]
# i=2: new_row = [1, 1, 1]
#      new_row[1] = row[0] + row[1] = 1 + 1 = 2
#      new_row = [1, 2, 1]
#      row = [1, 2, 1]
# i=3: new_row = [1, 1, 1, 1]
#      new_row[1] = row[0] + row[1] = 1 + 2 = 3
#      new_row[2] = row[1] + row[2] = 2 + 1 = 3
#      new_row = [1, 3, 3, 1]
#      row = [1, 3, 3, 1]
# Output: [1, 3, 3, 1]

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    rowIndex = 3
    result = sol.getRow(rowIndex)
    print("Pascal's Triangle row at index {}:".format(rowIndex))
    print(result)
    # Output:
    # Pascal's Triangle row at index 3:
    # [1, 3, 3, 1]
