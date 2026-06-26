class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 2 > len(nums) or len(nums) > 1000:
            return
        for idx_i, i in enumerate(nums):
            for idx_j, j in enumerate(nums):
                if idx_i != idx_j and i + j == target:
                    return [idx_i, idx_j]
