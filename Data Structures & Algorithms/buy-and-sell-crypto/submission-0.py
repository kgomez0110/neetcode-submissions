class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoney = 0
        currBuy = prices[0]
        left = right = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                maxMoney = max(prices[right] - prices[left], maxMoney)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return maxMoney
            


        