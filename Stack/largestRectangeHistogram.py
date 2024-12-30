class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = []
        pse = []
        stack = []
        for i in range(len(heights)):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if stack:
		            #store index instead of element
                pse.append(stack[-1][1])
            else:
                pse.append(-1)
            stack.append([heights[i],i])
  
        stack = []
        nse = [0] * len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1][1]
            else:
                nse[i] = -1
            stack.append([heights[i],i])
        answer = -float('inf')
        print(pse)
        print(nse)
        for i in range(len(heights)):
            previousSmaller = pse[i]
            nextSmaller = len(heights) if nse[i] == -1 else nse[i]
            print(previousSmaller,nextSmaller)
            area = heights[i] * (nextSmaller - previousSmaller -1)
            print(area)
            answer = max(answer,area)
        return answer

