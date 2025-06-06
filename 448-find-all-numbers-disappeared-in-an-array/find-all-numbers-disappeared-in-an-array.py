class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # ans = []

        # n = len(nums)
        # i = 1

        # while n > 0:
        #     if i not in nums:
        #         ans.append(i)
        #     i += 1
        #     n -= 1
        # return ans
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result        

