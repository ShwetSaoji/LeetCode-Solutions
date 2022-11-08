class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        temp = 0 
        for i in range(m, l):
            if temp == n:
                break
            else:
                nums1[i] = nums2[temp]
                temp += 1
        
        nums1.sort()
