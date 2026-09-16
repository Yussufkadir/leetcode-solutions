from typing import Optional
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.temp = 0
    def depth(n):
        if n is None:
            return 0
        left_traversal = depth(n.left)
        right_traversal = depth(n.right)
        self.temp = max(self.temp, left_traversal + right_traversal)
        return 1 + max(left_traversal, right_traversal)
    depth(root)
    return self.temp