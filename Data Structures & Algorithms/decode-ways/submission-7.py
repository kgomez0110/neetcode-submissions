class Solution:
    """
    base case:
    1 char -
        if 0 -> 0
        else n -> 1
    2 char - 
        if int(s) < 10 -> 0
        if int(s) > 26 -> 1
        else -> 2
    n
        helper(s-1) + helper(s-2) + base(s[-1]) + base(s[-2:])

    """
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.helper(s, memo)

    
    def helper(self, s: str, memo: dict) -> int:
        if s in memo: return memo[s]
        if len(s) <= 1:
            val = self.base(s)
            memo[s] = val
            return val
        lastDig = self.base(s[-1])
        lastTwo = self.base(s[-2:])
        lastDigHelper = self.helper(s[:-1], memo)
        lastTwoDigHelper = self.helper(s[:-2], memo)
        memo[s[:-1]] = lastDigHelper
        memo[s[:-2]] = lastTwoDigHelper
        if lastDig and lastTwo:
            return lastDigHelper + lastTwoDigHelper
        if lastDig:
            return lastDigHelper
        if lastTwo:
            return lastTwoDigHelper
        else:
            return 0

    @staticmethod
    def base(s: str) -> int:
        if len(s) == 0: return 1
        if len(s) == 1:
            if int(s) == 0: return 0
        if len(s) == 2:
            if int(s) < 10 or int(s) > 26: return 0
        return 1

        