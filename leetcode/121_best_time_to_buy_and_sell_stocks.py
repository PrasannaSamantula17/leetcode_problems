# Time omplexity - O(n)
# Space Complexity - O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate potential profit and update max_profit
            max_profit = max(max_profit, price - min_price)
            
        return max_profit
