# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.ans = None

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.n += 1
            if self.n == k:
                self.ans = root.val
                return

            inorder(root.right)
        inorder(root)
        return self.ans    



















        # n = 0
        # stack = []
        # curr = root 
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left


        #     curr = stack.pop()
        #     n += 1
        #     if n == k:
        #         return curr.val
        #     curr = curr.right        





























        
        
















        
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