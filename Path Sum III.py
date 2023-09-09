# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.d = {}
        self.count = 0
        self.targetSum = targetSum
        self.preorder(root, 0)
        return self.count

    def preorder(self, node, curr_sum):
        if node is None:
            return
        
        curr_sum += node.val

        if curr_sum == self.targetSum:
            self.count+= 1
        
        self.count += self.d.get(curr_sum - self.targetSum, 0)

        self.d[curr_sum] = self.d.get(curr_sum, 0) + 1

        self.preorder(node.left, curr_sum)
        self.preorder(node.right, curr_sum)

        self.d[curr_sum] -= 1
    


        
