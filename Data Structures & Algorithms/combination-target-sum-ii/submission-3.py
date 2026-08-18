class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(ii, subset, curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return
            if curr_sum > target or ii >= len(candidates): return
            subset.append(candidates[ii])
            dfs(ii + 1, subset, curr_sum + candidates[ii])
            subset.pop()
            while ii + 1 < len(candidates) and candidates[ii] == candidates[ii + 1]:
                ii += 1
            dfs(ii + 1, subset, curr_sum)
        dfs(0, [], 0)
        return result
        