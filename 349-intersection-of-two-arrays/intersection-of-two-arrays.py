class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] 
        ans = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        
        for i in nums2:
            if i in nums1:
                res.append(i)
        
        for i in res:
            if i in ans:
                continue
            else:
                ans.append(i)
        
        return ans