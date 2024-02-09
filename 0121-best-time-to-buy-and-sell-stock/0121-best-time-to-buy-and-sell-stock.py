class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue=prices[0]
        profit=0
        for i in prices:
            minValue=min(minValue, i)
            profit=max(i-minValue, profit)
        return profit