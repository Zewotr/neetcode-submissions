class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for indx, i in enumerate(nums):
            if target == i:
                return indx
        return -1
                
