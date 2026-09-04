# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #use dfs to check
        def dfs(node, ans):
            if not node:
                ans.append(None)
                return 
            ans.append(node.val)#add the current node
            dfs(node.left, ans)
            dfs(node.right, ans)
        
        ans1 = []
        ans2 = []
        dfs(p, ans1)
        dfs(q, ans2)
        return ans1 == ans2