class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k 
        rightEdge = len(nums)
        winMax = []
        currentWindow = []
        slidingWindowMax = []

        while right <= rightEdge:
            currentWindow = nums[left:right]
            winMax = max(currentWindow)

            slidingWindowMax.append(winMax)
            left = left + 1
            right = right + 1
        
        return slidingWindowMax