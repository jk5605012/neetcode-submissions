class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []