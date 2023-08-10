# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        n = head
        count = 0
        while n:
            count += 1
            n = n.next
        
        mid = count // 2

        prev, curr = None, head
        while mid != 0:
            prev = curr
            curr = curr.next
            mid -= 1
        prev.next = curr.next
        return head
