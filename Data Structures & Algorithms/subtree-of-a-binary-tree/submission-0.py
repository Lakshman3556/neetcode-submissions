# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        def same(p,q):
            if not p and not q:
                return True
            elif (not p and q) or (p and not q):
                return False    
            if p.val==q.val:
                return same(p.left,q.left) and same(p.right,q.right)
            else:
                return False
        def check(p,q):
            if not p:
                return False
            if same(p,q):
                return True
            return check(p.left,q) or check(p.right,q)    
        return check(root,subRoot)



