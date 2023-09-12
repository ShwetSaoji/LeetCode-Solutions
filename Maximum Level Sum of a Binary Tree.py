# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        q.append(None)

        maxSum = root.val
        level = 1
        curSum = 0
        res = 1

        while q:
           
            curr = q.popleft()
            if curr is not None:
                curSum += curr.val
                if curr.left:
                    q.append(curr.left)
                   
                if curr.right:
                    q.append(curr.right)
                    
            else:
                if curSum > maxSum:
                    maxSum = curSum
                    res = level
                curSum = 0
                level += 1
                if q:
                    q.append(None)
        
        return res
