# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ordered_list = []

        def inorder(root):
            if not root:
                return
            if root.left:
                inorder(root.left)
            # else:
            #     self.ordered_list.append(root.val)
            self.ordered_list.append(root.val)
            if root.right:
                inorder(root.right)
            # else:
            #     self.ordered_list.append(root.val)
        
        inorder(root)
        print(self.ordered_list)
        return self.ordered_list[:k][-1]