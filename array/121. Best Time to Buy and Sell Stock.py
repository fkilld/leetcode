class Solution(object):
    def maxProfit(self, prices):
        """
        Finds the maximum profit that can be achieved from a single buy and a single sell of stock.
        :type prices: List[int]
        :rtype: int
        """
        # Initialize the minimum price to a very large value (infinity)
        min_price = float('inf')
        # Initialize the maximum profit to 0
        max_profit = 0

        # Iterate through each price in the list
        for i, price in enumerate(prices):
            # If the current price is less than the minimum price seen so far, update min_price
            if price < min_price:
                min_price = price
                # Print debug info
                # print(f"Day {i}: New minimum price found: {min_price}")
            # Otherwise, calculate the profit if we sold at the current price
            else:
                profit = price - min_price
                # If this profit is greater than the max_profit so far, update max_profit
                if profit > max_profit:
                    max_profit = profit
                    # Print debug info
                    # print(f"Day {i}: New max profit found: {max_profit} (Sell at {price}, Buy at {min_price})")
        # Return the maximum profit found
        return max_profit

# Detailed Example:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Step-by-step:
# Day 0: price = 7, min_price = 7, max_profit = 0
# Day 1: price = 1, min_price = 1, max_profit = 0
# Day 2: price = 5, profit = 5 - 1 = 4, max_profit = 4
# Day 3: price = 3, profit = 3 - 1 = 2, max_profit = 4
# Day 4: price = 6, profit = 6 - 1 = 5, max_profit = 5
# Day 5: price = 4, profit = 4 - 1 = 3, max_profit = 5
# Output: 5

# Example usage and output:
if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    result = sol.maxProfit(prices)
    print("Maximum profit:", result)
    # Output:
    # Maximum profit: 5
