def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    final_list = []
    def traversal(n):
        if n is None:
            return
        traversal(n.left)
        final_list.append(n.val)
        traversal(n.right)
    traversal(root)
    return final_list