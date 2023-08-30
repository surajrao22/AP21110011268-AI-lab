class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def areMirrors(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.value == root2.value) and \
           areMirrors(root1.left, root2.right) and \
           areMirrors(root1.right, root2.left)

def isSymmetric(root):
    if root is None:
        return True
    return areMirrors(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)

print(isSymmetric(root))