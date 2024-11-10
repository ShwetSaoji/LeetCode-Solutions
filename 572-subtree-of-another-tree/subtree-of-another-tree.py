# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))
                


    def isSame(self, p , q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSame(p.left, q.left) and self.isSame(p.right, q.right))