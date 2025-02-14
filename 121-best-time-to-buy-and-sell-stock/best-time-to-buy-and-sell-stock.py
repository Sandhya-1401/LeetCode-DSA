class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Set an initially very high minimum price
        max_profit = 0  # Initialize max profit as 0

        for price in prices:
            if price < min_price:  # Update the minimum price found so far
                min_price = price
            elif price - min_price > max_profit:  # Check for max profit
                max_profit = price - min_price

        return max_profit  # Return the maximum profit found

# Example usage:
prices = [7, 1, 5, 3, 6, 4]  # Sample input
solution = Solution()
print(solution.maxProfit(prices))  # Output: 5
