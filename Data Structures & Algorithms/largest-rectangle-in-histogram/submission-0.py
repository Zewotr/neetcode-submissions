class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []              # stores indices
        max_area = 0

        heights.append(0)       # sentinel to empty the stack

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area