class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for ii in range(len(nums)):
            if target-nums[ii] in numMap: return [numMap[target-nums[ii]], ii]
            numMap[nums[ii]] = ii
        