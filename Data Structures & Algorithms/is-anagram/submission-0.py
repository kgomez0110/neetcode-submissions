class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sArr = self.makeCharArray(s)
        tArr = self.makeCharArray(t)
        return sArr == tArr
    def makeCharArray(self, string: str) -> list[int]:
        arr = [0 for i in range(26)]
        for c in string:
            arr[ord(c)%26] += 1
        return arr
        