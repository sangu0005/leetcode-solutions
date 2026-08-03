class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea

        # maxArea = 0
        # stk = []

        # for i, h in enumerate(heights):
        #     start = i
        #     while stk and stk[-1][1] > h:
        #         index, height = stk.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
        #     stk.append((start, h))

        # for i, h in stk:
        #     maxArea = max(maxArea,h * (len(heights) - i))
        # return maxArea