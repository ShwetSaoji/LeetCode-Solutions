# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0 
        self.preorder(root, root.val)
        return self.ans
    def preorder(self, root, max_val):
        if not root:
            return
        if root.val >= max_val:
            self.ans += 1
        max_val = max(max_val, root.val)
        self.preorder(root.left, max_val)
        self.preorder(root.right, max_val)
    