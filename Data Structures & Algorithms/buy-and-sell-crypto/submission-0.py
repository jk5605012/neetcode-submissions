class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                profit = prices[j] - prices[i]
                if profit > max_num:
                    max_num = profit
        return max_num