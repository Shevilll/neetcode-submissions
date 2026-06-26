class TreeNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def insertNode(root, key, val):
            if not root:
                return TreeNode(key, val)
            if root.key > key:
                root.left = insertNode(root.left, key, val)
            elif root.key < key:
                root.right = insertNode(root.right, key, val)

            return root

        self.root = insertNode(self.root, key, val)

    def get(self, key: int) -> int:
        def search(root, key):
            if not root:
                return -1
            elif root.key > key:
                return search(root.left, key)
            elif root.key < key:
                return search(root.right, key)
            else:
                return root.val

        return search(self.root, key)

    def getMin(self) -> int:
        def get_min(root):
            if not root:
                return -1
            if not root.left:
                return root.val
            return get_min(root.left)
        
        return get_min(self.root)

    def getMinKey(self, root) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.key

    def getMinVal(self, root) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        def get_max(root):
            if not root:
                return -1
            if not root.right:
                return root.val
            return get_max(root.right)
        
        return get_max(self.root)

    def remove(self, key: int) -> None:
        def remove_node(root, key):
            if not root:
                return root
            if root.key > key:
                root.left = remove_node(root.left, key)
            elif root.key < key:
                root.right = remove_node(root.right, key)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    minkey = self.getMinKey(root.right)
                    minval = self.getMinVal(root.right)
                    root.key = minkey
                    root.val = minval
                    remove_node(root.right, minkey)
            return root
        
        self.root = remove_node(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)
        
        inorder(self.root)
        return res


