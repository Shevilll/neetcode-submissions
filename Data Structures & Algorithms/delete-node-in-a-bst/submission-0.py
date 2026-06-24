# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr.val
        
        def remove(root, val):
            if not root:
                return root
            if root.val > val:
                root.left = remove(root.left, val)
            elif root.val < val:
                root.right = remove(root.right, val)
            else:
                if root.right and not root.left:
                    return root.right
                if root.left and not root.right:
                    return root.left
                if not root.left and not root.right:
                    return None
                
                minVal = findMin(root.right)
                root.val = minVal
                root.right = remove(root.right, minVal)
            return root
        
        return remove(root, key)