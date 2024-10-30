# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        track = []

        while head:
            if head in track:
                return True
            else:
                track.append(head)
                head = head.next
        
        return False