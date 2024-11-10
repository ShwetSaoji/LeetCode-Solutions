# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        
        # if root.val > p.val and root.val > q.val:
        #     self.lowestCommonAncestor(root.left, p, q)
        # elif root.val < p.val and root.val < q.val:
        #     self.lowestCommonAncestor(root.right, p, q)
        # elif (root.val == p.val or root.val == q.val):
        #     return root
        # else:
        #     return root
        
