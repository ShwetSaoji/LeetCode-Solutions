class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        mx = 0 
        for i in range(len(height)):
            if height[i] > mx:
                maxLeft[i] = height[i]
                mx = height[i]
            else:
                maxLeft[i] = mx
        
        mx = 0 

        for i in range(len(height)-1, -1, -1):
            if height[i] > mx:
                maxRight[i] = height[i]
                mx = height[i]
            else:
                maxRight[i] = mx
        
        ans = 0 

        for i in range(len(height)):
            ans = ans + min(maxLeft[i], maxRight[i]) - height[i]
        
        return ans