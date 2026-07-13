# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            l = preorder(p.left, q.left)
            r = preorder(p.right, q.right)
            if not l or not r:
                return False
            return True
        return preorder(p, q)