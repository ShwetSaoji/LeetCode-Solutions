# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def co(root, curmax):
            if root:
                #print(root.val)
                curmax = max(curmax, root.val)
                if curmax <= root.val:
                    #print(str(m) + "is greater or eq than" + str(root.val))
                    count[0] += 1
                if root.left:
                    co(root.left,curmax)
                if root.right:
                    co(root.right,curmax)
    

        co(root, 0)
        return count[0]
