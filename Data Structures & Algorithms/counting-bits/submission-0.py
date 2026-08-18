class Solution:
    """
    n = 16
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, , 16]
    [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2,  3,  2,  3,   3, 4,    1]

    0 -> 0
    1 -> 1
    2 -> 10
    3 -> 11
    4 -> 100   
    5 -> 101
    6 -> 110
    7 -> 111
    8 -> 1000 
    9 -> 1001
    10 -> 1010
    11 -> 1011
    12 -> 1100
    13 -> 1101,
    14 -> 1110
    """
    def countBits(self, n: int) -> List[int]:
        output = [0] * len(range(n+1))
        
        def bottom(k: int):
            if k == 0: return
            if output[k] != 0: return
            past_power_of_two = (1 << k.bit_length() - 1)
            if k == past_power_of_two: output[k] = 1
            else: output[k] = output[k - past_power_of_two] + 1
        for ii in range(n+1):
            bottom(ii)
        return output
        
        
        