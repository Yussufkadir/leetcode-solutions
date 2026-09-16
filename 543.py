from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
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

n1=TreeNode(1) 
n3=TreeNode(3)
n2=TreeNode(2,n1,n3)
n5=TreeNode(5)
root=TreeNode(4,n2,n5)
sol = Solution()
result = sol.diameterOfBinaryTree(root)
print(result)