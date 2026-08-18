class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(ii, curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return
            if curr_sum > target:
                return
            if ii >= len(nums):
                return
            subset.append(nums[ii])
            dfs(ii, curr_sum + nums[ii])
            subset.pop()
            dfs(ii + 1, curr_sum)
        dfs(0, 0)
        return result
        