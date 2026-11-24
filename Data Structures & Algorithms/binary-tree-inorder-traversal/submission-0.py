# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def io(root):
            if not root:
                return
            io(root.left)
            res.append(root.val)
            io(root.right)
        io(root)    
        return res        