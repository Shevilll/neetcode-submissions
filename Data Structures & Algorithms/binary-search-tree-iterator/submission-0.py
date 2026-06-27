# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.i = 0
        self.stack = []
        self.res = []
        self.inorder(self.root)

    def inorder(self, root):
        curr = self.root
        while curr or self.stack:
            if curr:
                self.stack.append(curr)
                curr = curr.left
            else:
                curr = self.stack.pop()
                self.res.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        temp = self.res[self.i]
        self.i += 1
        return temp

    def hasNext(self) -> bool:
        return self.i <= len(self.res) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()