class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = [False for i in range(len(strs))]
        anagrams = []
        charArrays = [self.makeCharArray(string) for string in strs]
        for ii in range(len(strs)):
            if seen[ii]: continue
            seen[ii] = True
            grouping = [strs[ii]]
            for jj in range(ii, len(strs)):
                if seen[jj]: continue
                if charArrays[ii] == charArrays[jj]:
                    seen[jj] = True
                    grouping.append(strs[jj])
            anagrams.append(grouping)
        return anagrams


    def makeCharArray(self, string: str) -> List[str]:
        arr = [0 for i in range(26)]
        for c in string:
            arr[ord(c) % 26] += 1
        return arr
        