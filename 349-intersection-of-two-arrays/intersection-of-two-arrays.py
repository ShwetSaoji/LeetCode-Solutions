class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] 

        for i in nums1:
            if i in nums2:
                res.append(i)
        
        for i in nums2:
            if i in nums1:
                res.append(i)
        
        return list(set(res))