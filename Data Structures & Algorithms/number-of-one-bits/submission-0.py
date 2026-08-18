class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for ii in range(32):
            if n & 1 == 1: total += 1
            n = n >> 1
        return total