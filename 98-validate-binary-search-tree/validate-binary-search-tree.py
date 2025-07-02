# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    def helper(self, root, left, right):
        if not root:
            return True
        if not (root.val > left and root.val < right):
            return False
        return self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right)



        # if not root:
        #     return
        # if root.left and root.left.val >= root.val:
        #     return False
        # elif root.right and root.right.val <= root.val:
        #     return False 
        # else:
        #     return True
        # return self.isValidBST(root.left) and self.isValidBST(root.right)