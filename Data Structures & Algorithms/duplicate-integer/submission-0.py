class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_arr = Counter(nums)
        print(count_arr)
        for i in count_arr.values():
            if i > 1:
                return True
        return False