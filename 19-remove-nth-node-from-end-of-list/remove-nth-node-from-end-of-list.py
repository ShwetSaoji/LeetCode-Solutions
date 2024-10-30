# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 0 
        dummy = head
        while dummy:
            ll_len += 1
            dummy = dummy.next
        if ll_len <= 1:
            return None
        index_to_be_deleted = ll_len - n
        if index_to_be_deleted == 0:
            head = head.next
            return head
        dummy = head
        while index_to_be_deleted > 1:
            dummy = dummy.next
            index_to_be_deleted -= 1
        
        dummy.next = dummy.next.next
        return head