class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        def check(root):
            if not root:
                return True
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh - rh) > 1:
                return False
            left = check(root.left)
            right = check(root.right)
            if not left or not right:
                return False
            return True
        return check(root)