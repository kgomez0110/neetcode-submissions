class Solution:
    """
    start at the amount
    for each coin you can either take that coin, 
        increase the total number of coins and decrease that coin value from the total ammount
        skip that coin

    """
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = {}
    #     def helper(n: int) -> int:
    #         if n in memo: return memo[n]
    #         if n == 0: return 0
    #         if n < 0: return float('inf')
    #         best = min([helper(n-c) + 1 for c in coins], default=float('inf'))
    #         memo[n] = best
    #         return best
    #     min_coins = helper(amount)
    #     if min_coins == float('inf'): return -1
    #     return min_coins

    """
    building an array with the possible values of n
    at each interval:
        for each coin:
            subtract that coin value from the index
            hop to that index, add the value in it. that value is the min coins
            get the min value
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        def helper(coin: int, ii: int) -> int:
            if ii - coin < 0: return float('inf')
            return dp[x-coin]

        for x in range(1, amount+1):
            dp[x] = min(helper(c, x) + 1 for c in coins)
        return -1 if dp[amount] == float('inf') else dp[amount]

