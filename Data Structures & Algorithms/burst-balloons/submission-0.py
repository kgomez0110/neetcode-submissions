class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[left, right]
            memo[(left, right)] = 0
            for ii in range(left, right+1):
                coins = nums[left - 1] * nums[ii] * nums[right + 1]
                coins += dfs(ii+1, right) + dfs(left, ii-1)
                memo[(left, right)] = max(coins, memo[(left, right)])
            return memo[(left, right)]
        
        return dfs(1, len(nums) - 2)