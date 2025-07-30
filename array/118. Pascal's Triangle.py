class Solution(object):
    def generate(self, numRows):
        """
        Generate the first numRows of Pascal's Triangle.
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Initialize the result list that will contain all rows of Pascal's Triangle
        result = []
        
        # Loop through each row index from 0 to numRows-1
        for i in range(numRows):
            # Start each row with a list of 1s (since first and last elements are always 1)
            row = [1] * (i + 1)
            
            # Fill in the inner elements of the row (if any)
            # The first and last elements are always 1, so we start from 1 and end at i-1
            for j in range(1, i):
                # Each element is the sum of the two elements above it in the previous row
                row[j] = result[i-1][j-1] + result[i-1][j]
            
            # Append the constructed row to the result
            result.append(row)
        
        # Return the complete Pascal's Triangle up to numRows
        return result

# Detailed Example:
# Input: numRows = 5
# Step-by-step:
# i=0: row = [1]                           -> result = [[1]]
# i=1: row = [1, 1]                        -> result = [[1], [1, 1]]
# i=2: row = [1, 1, 1]
#       row[1] = result[1][0] + result[1][1] = 1 + 1 = 2
#       row = [1, 2, 1]                    -> result = [[1], [1, 1], [1, 2, 1]]
# i=3: row = [1, 1, 1, 1]
#       row[1] = result[2][0] + result[2][1] = 1 + 2 = 3
#       row[2] = result[2][1] + result[2][2] = 2 + 1 = 3
#       row = [1, 3, 3, 1]                 -> result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
# i=4: row = [1, 1, 1, 1, 1]
#       row[1] = result[3][0] + result[3][1] = 1 + 3 = 4
#       row[2] = result[3][1] + result[3][2] = 3 + 3 = 6
#       row[3] = result[3][2] + result[3][3] = 3 + 1 = 4
#       row = [1, 4, 6, 4, 1]              -> result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    triangle = sol.generate(numRows)
    print("Pascal's Triangle with numRows = {}:".format(numRows))
    for row in triangle:
        print(row)
    # Output:
    # Pascal's Triangle with numRows = 5:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
