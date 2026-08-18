from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []
        def dfs(ii: int):
            if ii >= len(nums):
                subsets.append(curr.copy())
                return
            curr.append(nums[ii])
            dfs(ii + 1)
            curr.pop()
            dfs(ii + 1)
        dfs(0)
        return subsets
