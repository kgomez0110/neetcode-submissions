class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
        
    def helper(self, n:int, memo: dict) -> int:
        if n == 0: return 1
        if n < 0: return 0
        if n in memo: return memo[n]
        val = self.helper(n-1, memo) + self.helper(n-2, memo)
        memo[n] = val
        return val
        