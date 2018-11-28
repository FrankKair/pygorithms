class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        def _insert(val, node):
            if val == node.val: return
            if val < node.val:
                if not node.left:
                    node.left = Node(val)
                else:
                    _insert(val, node.left)
            if val > node.val:
                if not node.right:
                    node.right = Node(val)
                else:
                    _insert(val, node.right)

        _insert(val, self.root)

    def inorder_traversal(self):
        def _inorder_traversal(node):
            if not node: return
            _inorder_traversal(node.left)
            print(node.val)
            _inorder_traversal(node.right)
        
        _inorder_traversal(self.root)
        

t = BinaryTree(5)
t.insert(4)
t.insert(2)
t.insert(1)
t.insert(6)
t.insert(3)
t.insert(14)
t.insert(7)
t.insert(0)
t.inorder_traversal()
