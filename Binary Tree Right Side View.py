# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque([root, None,])
        ans = []
        curr = root
        while q:
            prev , curr = curr, q.popleft()

            while curr:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev, curr = curr, q.popleft()
            
            ans.append(prev.val)
            if q:
                q.append(None)
        
        return ans
