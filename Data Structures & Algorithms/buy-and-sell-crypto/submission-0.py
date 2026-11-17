class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        entry_idx = 0
        max_profit = 0

        for i in range(len(prices)):
            
            if prices[i] < prices[entry_idx]:
                entry_idx = i

            diff = prices[i] - prices[entry_idx]

            if diff > max_profit:
                max_profit = diff

        return max_profit