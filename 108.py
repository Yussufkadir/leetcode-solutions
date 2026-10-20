def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
    def transform(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        m = nums[mid]
        node = TreeNode(m)
        node.left = transform(lo , mid - 1)
        node.right = transform (mid + 1, hi)
        return node
    return transform(0, len(nums) - 1)