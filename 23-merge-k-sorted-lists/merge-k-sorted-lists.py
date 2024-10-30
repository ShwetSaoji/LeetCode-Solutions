# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final_list = []
        self.head = None
        for i in lists:
                while i is not None:
                    final_list.append(i.val)
                    i = i.next
        
        # if final_list:
        #     self.head = ListNode(final_list[0])
        # print(self.head.val)
        final_list.sort()
        dummy = ListNode()
        # if final_list:
        #     head_node.val = final_list[0]
        head_node = dummy
        for i in range(len(final_list)):
            new_node = ListNode()
            new_node.val = final_list[i]
            head_node.next = new_node
            head_node = new_node
        return dummy.next