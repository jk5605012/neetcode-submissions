class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_n = nums[0]
        for i in range(len(nums)):
            s = nums[i]            
            for j in range(i+1, len(nums)):
                s += nums[j]
                if max_n < s:
                    max_n = s
                    print(max_n)
            if max_n < s:
                    max_n = s
                    print(max_n)
        return max_n