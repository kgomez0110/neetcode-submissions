import math
class Solution:
    """
   0 [1, 2, 0]
   1 [0, 1, 2]
   2 [2, 0, 1]
   3 [1, 2, 0]
   4 [0, 1, 2]
   5 [2, 0, 1]
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, remaining):
            if len(remaining) == 0:
                result.append(path[:])
            for ii in range(len(remaining)):
                path.append(remaining[ii])
                newRemaining = remaining[0:ii] + remaining[ii+1:]
                backtrack(path, newRemaining)
                path.pop()
        backtrack([], nums)
        return result
        