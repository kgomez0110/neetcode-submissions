class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for ii in range(32):
            val = (n >> ii) & 1
            mask = val << (31 - ii)
            result |= mask
        return result

        