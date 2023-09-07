# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res

    def dfs(self, node, tar, cur ):
        if node is None:
            return 

        cur.append(node.val)
        if node.left is None and node.right is None and node.val == tar:
            self.res.append(cur.copy()) 

        self.dfs(node.left, tar - node.val, cur)
        self.dfs(node.right, tar - node.val, cur)   
        cur.pop() 
