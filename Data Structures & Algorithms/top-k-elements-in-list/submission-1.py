class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        print(nums_count)
        freqs = [[] for _ in range(len(nums)+1)]
        res = []
        for n, v in nums_count.items():
            freqs[v].append(n)
        for i in range(len(freqs)-1, 0, -1):
            for j in freqs[i]:
                res.append(j)
            if k == len(res):
                return res
        return res