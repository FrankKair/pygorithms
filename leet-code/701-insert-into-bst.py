# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while True:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right

            else:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
 
        return root
