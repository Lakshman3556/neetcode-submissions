# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=0
        if not root:
            return 0
        def md(root,c):
            nonlocal d
            if root==None:
                d=max(d,c)
                return
            md(root.left,c+1)
            md(root.right,c+1)
        md(root,0)    
        return d           