class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        print(nums_count)
        a = nums_count.most_common()
        a = [a[i][0] for i in range(k)]
        return a