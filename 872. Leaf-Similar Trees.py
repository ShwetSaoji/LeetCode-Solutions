# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []

        self.traverse(root1, list1)
        self.traverse(root2, list2)
        return list1 == list2

    def traverse(self, root, arr):
        if root:
            if not root.left and not root.right:
                arr.append(root.val)
            if root.left:
                self.traverse(root.left, arr)
            if root.right:
                self.traverse(root.right, arr)
