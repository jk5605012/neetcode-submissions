import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:        
        cell = []
        res = []

        def rec(t, i):
            if t == 0:
                res.append(copy.deepcopy(cell))
                return
            if t < 0:
                return
            for j in range(i, len(nums)):
                cell.append(nums[j])
                rec(t - nums[j], j)
                cell.pop()
            
        rec(target, 0)
        return res
