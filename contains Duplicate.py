class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        dic = {}
        
        for i, n in enumerate(nums):
            #print(n)
            if n  in dic:
                return True
            else:
                dic[n] = i
                #print(dic)
                
        
        return False
