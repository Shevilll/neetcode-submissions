# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root 
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left


            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right        





























        
        # stack = []
        # current = root

        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     k -= 1

        #     if k == 0:
        #         return current.val
        #     current = current.right        
         
























        
        # t = 0
        # ans = -1

        # def dfs(root, k):
        #     nonlocal t, ans
        #     if not root:
        #         return

        #     dfs(root.left, k)
        #     t += 1
        #     if k == t:
        #         ans = root.val
        #         return
        #     dfs(root.right, k)

        # dfs(root, k)
        # return ans