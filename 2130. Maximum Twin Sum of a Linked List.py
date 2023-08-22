# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        n = head
        while n:
            arr.append(n.val)
            n = n.next
        print(arr)
        msum = 0
        for i in range(0, len(arr)//2):
            twin = len(arr) - 1 - i
            s = arr[i] + arr[twin]
            msum = max(s, msum)
        return msum
