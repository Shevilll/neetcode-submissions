from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        result = []
       

        while queue:
            level = []
          

            for i in range (len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            result.append(level)

        return result                

        

        
          





        # res = []

        # q = deque()
        # q.append(root)

        # while q:
        #     temp = []
        #     l = len(q)

        #     for i in range(l):
        #         curr = q.popleft()
        #         if curr:
        #             temp.append(curr.val)
        #             q.append(curr.left)
        #             q.append(curr.right)
        #     if temp:
        #         res.append(temp)

        # return res