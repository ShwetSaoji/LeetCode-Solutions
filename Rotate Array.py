class Solution:

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Below solution is a brute force approach. Time Limit excedded. 


        # temp = [0] * len(nums)
        # a = 0
        # #print(temp)
        # while k != 0:
        #     temp[0] = nums[-1]
        #     for i in range(1, len(nums)):
        #         temp[i] = nums[i-1]
        #    # print(temp)
        #     nums[:] = temp
        #    # print(nums)
        #     temp = [0] * len(nums)
        #     k -= 1

        ###################################################
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)   
