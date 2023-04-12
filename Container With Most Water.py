class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0 , len(height) -1 #two end pointers

        while l < r:
            area = (r-l)* min(height[l],height[r])
            res = max(area,res)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:   #if both pointers are equal.
                r -= 1
        return res
