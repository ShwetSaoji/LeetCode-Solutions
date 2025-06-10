# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        l1curr = list1
        l2curr = list2

        while l1curr and l2curr:
            if l1curr.val > l2curr.val:
                res.next = l2curr
                l2curr = l2curr.next
            else:
                res.next = l1curr
                l1curr = l1curr.next
            res = res.next
        
        while l1curr:
            res.next = l1curr
            l1curr = l1curr.next
            res = res.next
        
        while l2curr:
            res.next = l2curr
            l2curr = l2curr.next
            res = res.next

        return head.next