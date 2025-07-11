# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0 
        # self.max_val = 0 
        def isgood(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.res += 1
            max_val = max(max_val, node.val)
            isgood(node.left, max_val)
            isgood(node.right, max_val)

        isgood(root, root.val)
        return self.res