# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q == None and p== None:
            return True
        if (q == None and p!=None) or (q!=None and p==None):
            return False
        a=1    
        def check(p,q):
            nonlocal a
            if p==None and q==None:
                return
            if p == None or q == None:
                a = 0
                return    
            if p.val!=q.val:
                a=0           
            check(p.left,q.left)
            check(p.right,q.right)
        check(p,q)    
        if a==1:
            return True
        else:
            return False            