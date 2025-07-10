"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashMap = {None:None}
        while curr:
            newNode = Node(curr.val)
            hashMap[curr] = newNode
            curr = curr.next


        curr = head
        while curr:
            copy = hashMap[curr]
            copy.next = hashMap[curr.next]
            copy.random = hashMap[curr.random]
            curr = curr.next
        
        return hashMap[head]