class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def pre_order_traversal(node):
    if node:
        print(node.val, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    pre_order_traversal(root)
    print()
