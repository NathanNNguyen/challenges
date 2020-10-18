class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def isValidBST(node):
    return is_bst(node, float('-inf'), float('inf'))


def is_bst(root, minVal=float('-inf'), maxVal=float('inf')):
    if root is None:
        return True
    if root.key <= minVal or root.key >= maxVal:
        return False
    validLeft = is_bst(root.left, minVal, root.key)
    validRight = is_bst(root.right, root.key, maxVal)
    return validLeft and validRight


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
# 1  4 6
