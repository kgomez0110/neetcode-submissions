from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(curr: List[int], ii:int):
            if ii >= len(nums):
                subsets.append(curr.copy())
                return
            curr.append(nums[ii])
            dfs(curr, ii+1)

            curr.pop()
            dfs(curr, ii+1)
        dfs([], 0)
        return subsets
