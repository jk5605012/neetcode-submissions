class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            # Option 1: Rob current house and move to i+2
            # Option 2: Skip current house and move to i+1
            res = max(nums[i] + dfs(i + 2), dfs(i + 1))
            memo[i] = res
            return res
            
        return dfs(0)