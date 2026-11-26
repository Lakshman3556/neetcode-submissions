# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        if not root:
            return 0
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        def check(root):
            nonlocal maxi
            if not root:
                return
            lh=height(root.left)
            rh=height(root.right)
            maxi=max(maxi,lh+rh)
            check(root.left)
            check(root.right)
        check(root)
        return maxi  