import math
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, remaining):
            if len(remaining) == 0:
                result.append(path.copy())
                return
            for ii in range(len(remaining)):
                path.append(remaining[ii])
                backtrack(path, remaining[:ii] + remaining[ii+1:])
                path.pop()
        backtrack([], nums)
        return result


