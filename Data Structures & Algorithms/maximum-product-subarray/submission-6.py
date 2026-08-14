from math import prod
class Solution:
    """
    at every step i can either include it to the current sub array
    or make a new one or remove the first number in the array

    [1, -222, 1, 1, -3]
    """

    def maxProduct(self, nums: List[int]) -> int:
        best = curr_max = curr_min = nums[0]
        for ii in range(1, len(nums)):
            temp_curr_max = max(nums[ii], nums[ii]*curr_max, nums[ii]*curr_min)
            curr_min = min(nums[ii], nums[ii]*curr_max, nums[ii]*curr_min )
            best = max(temp_curr_max, best)
            curr_max = temp_curr_max
        return best