# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, target, val):
            if not root:
                return False
            val += root.val
            if not root.left and not root.right:
                return target == val
            if dfs(root.left, target, val):
                return True
            if dfs(root.right, target, val):
                return True
            return False
        
        return dfs(root, targetSum, 0)