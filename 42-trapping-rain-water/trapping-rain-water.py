class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = [0] * len(height)
        minLeftRight = [0] * len(height)
        mx = 0

        for i in range(len(height)):
            mx = max(mx, height[i])
            maxLeft.append(mx)
        mx = 0
        for i in range(len(height)-1,-1,-1):
            mx = max(mx, height[i])
            maxRight[i] = mx
            minLeftRight[i] = min(maxRight[i], maxLeft[i])
        
        ans = 0 

        for i in range(len(height)):
            if minLeftRight[i] - height[i] > 0:
                ans += minLeftRight[i] - height[i]
        return ans

