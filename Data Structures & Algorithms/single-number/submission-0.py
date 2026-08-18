class Solution:
    """
    3 -> 11
    2 -> 10
    """

    def singleNumber(self, nums: List[int]) -> int:
        first = nums[0]
        for ii in range(1, len(nums)):
            first = first ^ nums[ii]
        return first

        