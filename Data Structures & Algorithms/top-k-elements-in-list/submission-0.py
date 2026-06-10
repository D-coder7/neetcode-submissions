from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        ans = dict(sorted(count.items(), key=itemgetter(1), reverse=True))
        #print(ans)
        return list(ans.keys())[:k]