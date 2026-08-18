class Solution:
    """
    [0, 1, 3]
    0 -> 00
    1 -> 01
    2 -> 10
    3 -> 11
    """

    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        for ii in range(len(nums) + 1):
            start ^= ii
        for ii in range(len(nums)):
            start ^= nums[ii]
        return start