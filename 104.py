def maxDepth(self, root: TreeNode | None) -> int:
    def traversal(n):
        if n is None:
            return 0
        left_traversal = traversal(n.left)
        right_traversal = traversal(n.right)
        return 1 + max(left_traversal, right_traversal)
    return traversal(root)