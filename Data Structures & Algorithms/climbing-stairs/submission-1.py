class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(d):
            if d == 1 or d == 0:
                return 1
            if d in memo:
                return memo[d]
            memo[d] = rec(d-1) + rec(d-2)
            return memo[d]
        return rec(n)