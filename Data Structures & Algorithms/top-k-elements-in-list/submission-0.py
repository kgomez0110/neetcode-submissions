
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ii = 1
        topK = []
        frequency = 1
        while ii < len(nums):
            if nums[ii] == nums[ii-1]: frequency += 1
            else:
                heapq.heappush_max(topK, (frequency, nums[ii-1]))
                frequency = 1
            ii += 1
        heapq.heappush_max(topK, (frequency, nums[-1]))
        return [tup[1] for tup in heapq.nlargest(k, topK, self.getHeapKey)]
    
    @staticmethod
    def getHeapKey(tup):
        return tup[0]
        


        