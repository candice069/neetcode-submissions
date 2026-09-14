# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.getDepth(root.left)
        if left_height == -1:
            return -1
        right_height =self.getDepth(root.right)
        if right_height == -1:
            return -1
        if abs(left_height -right_height) > 1:
            return -1
        return 1+max(left_height, right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.getDepth(root)
        return False if height == -1 else True
        