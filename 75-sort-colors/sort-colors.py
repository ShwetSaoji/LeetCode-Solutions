class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort_color(curr, arr, l):
            for r in range(len(arr)):
                if arr[r] == curr:
                    arr[r], arr[l] = arr[l], arr[r]
                    l += 1
            return [arr, l]
        
        arr, l = sort_color(0, nums, 0)
        arr, l = sort_color(1, arr, l)