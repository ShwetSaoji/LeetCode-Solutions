# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.dfs(root)
        return ans[0]
    
    def dfs(self, curr):
        if not curr:
            return [True, 0]
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)
        balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balance, 1 + max(left[1], right[1])]