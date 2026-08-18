class Solution:
    def findMin(self, nums: List[int]) -> int:
        # pivot = len(nums) // 2
        # first = nums[0]
        # while pivot+1 < len(nums) and pivot > 0 and nums[pivot] < nums[pivot+1]:
        #     if nums[pivot] > first:
        #         pivot += len(nums[pivot:]) // 2
        #     else:
        #         pivot -= len(nums[0:pivot]) // 2
        # if pivot+1 < len(nums): return nums[pivot+1]
        # if pivot == 0: return nums[-1]
        # return nums[0]

        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high + low) // 2
            if nums[mid] > nums[high]: low = mid + 1
            else: high = mid
        return nums[low]
        