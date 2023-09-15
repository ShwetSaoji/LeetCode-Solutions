class Solution:
    def findKthLargest(self, nums, k):
        def quick(nums, k):
            pivot = random.choice(nums)
            left, right, mid = [], [] , []
            print(pivot)
            for i in nums:
                if i > pivot:
                    left.append(i)
                elif i < pivot:
                    right.append(i)
                else:
                    mid.append(i)
            
            if k <= len(left):
                return quick(left, k)
            
            if k > len(left) + len(mid):
                return quick(right, k - len(left) - len(mid))

            return pivot
        
        return quick(nums, k)
