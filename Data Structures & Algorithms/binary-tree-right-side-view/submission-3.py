# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        q = deque()
        q.append(root)

        while q:
            l = len(q)
            r = None
            for i in range(l):
                curr = q.popleft()
                if curr:
                    r = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if r:
                ans.append(r.val)
            
        return ans