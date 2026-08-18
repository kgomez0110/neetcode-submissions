class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       result = []
       nums.sort()
       def dfs(ii, subset):
            if ii >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[ii])
            dfs(ii + 1, subset)
            subset.pop()
            while ii + 1 < len(nums) and nums[ii] == nums[ii + 1]:
                ii += 1
            dfs(ii + 1, subset)
       dfs(0, [])
       return result